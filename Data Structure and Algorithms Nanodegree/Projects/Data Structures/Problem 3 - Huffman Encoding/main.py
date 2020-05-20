import argparse
import sys

from huffman import HuffmanTree


def huffman_encoding(text):
    if not text:
        raise ValueError("Text is empty. Abort encoding.")

    tree = HuffmanTree()
    tree.grow(text).encode()
    char_code = tree.get_mapping()

    res = ""
    for char in text:
        try:
            code = char_code[char]
        except:
            raise KeyError(
                f"{char} does not exist in the mapping. Abort encoding.")
        res += code

    return res, tree


def huffman_decoding(text, tree):
    res = ""
    idx = 0

    while idx < len(text):
        node = tree.get_root()

        while not node.is_leaf():
            if text[idx] == "0":
                node = node.get_left_child()
            elif text[idx] == "1":
                node = node.get_right_child()
            else:
                raise ValueError("Degenerate text to decode. Abort decoding.")
            idx += 1

        res += node.get_char()

    return res


def go(text, debug=False):
    if debug:
        print("The content of raw text is: {}".format(text))
        print(
            "The size of the raw text is: {}\n".format(sys.getsizeof(text)))

    encoded_text, tree = huffman_encoding(text)
    if debug:
        print("The content of the encoded text is: {}".format(encoded_text))
        print("The size of the encoded text is: {}\n".format(
            sys.getsizeof(int(encoded_text, base=2))))

    decoded_text = huffman_decoding(encoded_text, tree)
    if debug:
        print("The content of the encoded text is: {}".format(decoded_text))
        print("The size of the decoded text is: {}\n".format(
            sys.getsizeof(decoded_text)))

    return encoded_text, decoded_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', dest='text', type=str, default='Hello World!',
                        help=("The text message used to illustrate encoding "
                              "and decoding process."))
    args = parser.parse_args()

    go(args.text, debug=True)
