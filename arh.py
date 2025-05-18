#!/usr/bin/python3

import argparse

from command import compress_methods, decompress_methods, view_methods
from compress import Compress
from decompress import Decompress
from viewarchive import ViewArhive


def main():
    parser = argparse.ArgumentParser(description="Simple archiving tool")

    parser.add_argument(
        "method",
        choices=["tar", "tar.bz2", "tar.gz", "tar.xz", "zip", "rar", "7z"],
        help="method",
    )

    parser.add_argument(
        "operation",
        choices=["pack", "unpack", "list"],
        help="Type operation",
    )

    parser.add_argument(
        "-o", "--output", default="archive", required=True, help="output name"
    )

    parser.add_argument("-s", "--silent", action="store_true", help="silent mode")

    parser.add_argument("files", nargs="*", help="files")

    args = parser.parse_args()

    files = " ".join(args.files)

    match args.operation:
        case "pack":
            method = compress_methods.get(args.method)
            if method:
                getattr(Compress(files, args.output, args.silent), method)()

        case "unpack":
            method = decompress_methods.get(args.method)
            if method:
                getattr(Decompress(files, args.output, args.silent), method)()

        case "list":
            method = view_methods.get(args.method)
            if method:
                getattr(ViewArhive(files), method)()


if __name__ == "__main__":
    main()
