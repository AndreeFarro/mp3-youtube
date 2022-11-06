def clean_format_filename(filename):
    return filename.split("temp\\")[1].replace("\\","/").rsplit( ".", 1 )[0]