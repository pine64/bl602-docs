import sys
import os
import logging
import argparse
import glob
import re

from googletrans import Translator

import sphinx.parsers
import docutils
import docutils.nodes

from dataclasses import dataclass
from typing import List

if sys.version_info.major != 3:
    logging.fatal(f"`{__file__}` requires python 3 to run")

# Path of this file
self_file_path = os.path.dirname(os.path.realpath(__file__))
DOCS_DIR = os.path.abspath(os.path.join(self_file_path, "..", "src"))

# Argument parsing
args_parser = argparse.ArgumentParser(description="Translate documentation from source "
        "language to 'destination' language")
args_parser.add_argument("source_lang", type=str, help="The language to translate from")
args_parser.add_argument("dest_lang", type=str, help="The language to translate to")

args = args_parser.parse_args(sys.argv[1:])

source_lang_dir = os.path.join(DOCS_DIR, args.source_lang)
dest_lang_dir = os.path.join(DOCS_DIR, args.dest_lang)

if not os.path.isdir(source_lang_dir):
    logging.fatal(f"Directory {source_lang_dir} (SOURCE_LANG) does not exist")

if os.path.isdir(dest_lang_dir):
    logging.warning(f"Directory {dest_lang_dir} (DEST_LANG) already "
        "exists. Will retranslate.")
else:
    os.mkdir(dest_lang_dir)

"""
How this works:
1. We recursively iterate all the .rst files within `source_lang_dir`
   and parse each file.
2. All text nodes that should be translated (non-code nodes) are collected
   and assigned an ID in a roster object.
3. We take a batch of `n` paragraphs from the roster object and translate them
4. After all the batches are translated, We recreate these nodes for
   files in `dest_lang_dir`
"""

rst_parser = sphinx.parsers.RSTParser()
translator = Translator()

rst_parser_settings = docutils.frontend.OptionParser(
    components=(docutils.parsers.rst.Parser,)
).get_default_values()

@dataclass
class TranslationQueueElement:
    node: docutils.nodes.Node
    node_id: str
    original_text: str
    original_lang: str
    destination_text: str
    destination_lang: str

# Contains rst nodes of all files in `source_lang_dir`
node_translation_queue: object = {}

def make_text_from_queue() -> str:
    global node_translation_queue
    texts = []
    for node in node_translation_queue.values():
        texts.append(node.original_text)

    return "\n".join(texts)

def mutate_queue_with_text(text: str):
    global node_translation_queue
    parts = text.split("&e")
    for part in parts:
        # `part` is of the format <node_id>.:<translated_text>

        node_id = str(part[:part.find(".:")])
        translated_text = part[part.find(".:") + 2:].strip()
        node_translation_queue[node_id].destination_text = translated_text

# This class is responsible for collecting all the text nodes that
# need to be translated
class NodeTranslationVisitor(docutils.nodes.NodeVisitor):
    _counter = 0

    def add_to_translation_queue(self, node: docutils.nodes.Node):
        node_translation_queue[str(self._counter)] = TranslationQueueElement(
            node = node,
            node_id = self._counter,
            original_text = f"{self._counter}.:{node.astext()} &e",
            original_lang = args.source_lang,
            destination_text = "",
            destination_lang = args.dest_lang,
        )

    def dispatch_visit(self, node: docutils.nodes.Node):
        # Increment the counter on every step
        self._counter += 1

        # Here is where we start saving suitable text into the translation queue
        if isinstance(node, docutils.nodes.Text) or\
           isinstance(node, docutils.nodes.literal) or\
           isinstance(node, docutils.nodes.paragraph) or\
           isinstance(node, docutils.nodes.list_item) or\
           isinstance(node, docutils.nodes.bullet_list) or\
           isinstance(node, docutils.nodes.section) or\
           isinstance(node, docutils.nodes.title):
            self.add_to_translation_queue(node)

# This class is responsible for substituting the old text with the new
# translated text
class NodeMutationVisitor(docutils.nodes.NodeVisitor):
    _counter = 0

    def dispatch_visit(self, node: docutils.nodes.Node):
        # Increment the counter on every step
        self._counter += 1
        cur_node_id = str(self._counter)
        if node_translation_queue.get(cur_node_id) is not None:
            # This node has translated text to be injected
            # node.something = node_translation_queue[cur_node_id].destination_text
            pass

for filename in glob.glob(os.path.join(source_lang_dir, "**", "*.rst"), recursive=True):
    try:
        file = open(filename, "r")
        doc = docutils.utils.new_document(filename, rst_parser_settings)
        contents = file.read()
        file.close()

        # Until we can parse the `toctree` directive, we need to skip it
        if "toctree" in contents:
            continue

        rst_parser.parse(contents, doc)

        nv = NodeTranslationVisitor(doc)
        doc.walk(nv)

        # # After we've finished walking this file, we translate it
        # translations = translator.translate(
        #     make_text_from_queue(), src=args.source_lang, dest=args.dest_lang)

        # # Mutate the nodes in **translation queue** with the translated text
        # mutate_queue_with_text(translations.text)

        # Walk over again to inject the new translation from the queue
        translated_doc = doc.deepcopy()
        nv = NodeMutationVisitor(translated_doc)
        translated_doc.walk(nv)
        
        new_file_path = re.findall("/%s/[a-zA-Z0-9/]+\.rst$" % (args.source_lang), filename)[0]
        new_file_path = os.path.join(DOCS_DIR, args.dest_lang, "/".join(new_file_path.split("/")[2:]))

        # Finally, save the file under the new translated directory
        if not os.path.isdir("/".join(new_file_path.split("/")[:-1])):
            # TODO: Clean up this mess
            os.makedirs("/".join(new_file_path.split("/")[:-1]))

        translated_file = open(os.path.join(dest_lang_dir, new_file_path), "w")
        translated_file.write(translated_doc.astext())
        translated_file.close()

        break
    except Exception as e:
        logging.fatal(e)
        break
