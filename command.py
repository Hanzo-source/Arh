compress_methods = {
    "tar": "tar_compress",
    "tar.bz2": "tar_bz2_compress",
    "tar.gz": "tar_gz_compress",
    "tar.xz": "tar_xz_compress",
    "zip": "zip_compress",
    "rar": "rar_compress",
    "7z": "sevenzip_compress",
}

decompress_methods = {
    "tar": "tar_decompress",
    "tar.bz2": "tar_bz2_decompress",
    "tar.gz": "tar_gz_decompress",
    "tar.xz": "tar_xz_decompress",
    "zip": "zip_decompress",
    "rar": "rar_decompress",
    "7z": "sevenzip_decompress",
}

view_methods = {
    "tar": "tar_view",
    "zip": "zip_view",
    "rar": "rar_view",
    "7z": "sevenzip_view",
}


compress_cmd = {
    "tar": "tar -cvf",
    "tar_bz2": "tar -cjvf",
    "tar_gz": "tar -czvf",
    "tar_xz": "tar -cJvf",
    "zip": "zip",
    "zip_dir": "zip -r",
    "rar": "rar a",
    "sevenzip": "7z a",
}

decompress_cmd = {
    "tar": "tar -xvf",
    "tar_bz2": "tar -xjvf",
    "tar_gz": "tar -xzvf",
    "tar_xz": "tar -xJvf",
    "zip": "unzip -d",
    "rar": "unrar x",
    "sevenzip": "7z x",
}

view_cmd = {"tar": "tar -tvf", "zip": "unzip -l", "rar": "unrar l", "7z": "7z l"}
