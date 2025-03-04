TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 800,
    'plugins': '''
        advlist autolink lists link image imagetools charmap print preview anchor
        searchreplace visualblocks insertdatetime table paste help wordcount
    ''',
    'toolbar1': '''
        undo redo | formatselect fontsizeselect | bold italic underline |
        alignleft aligncenter alignright alignjustify | bullist numlist |
        link image | preview fullscreen
    ''',
    'images_upload_url': '/core/upload-image/',  # ✅ Umumiy rasm yuklash URL
    'automatic_uploads': True,
    'file_picker_types': 'image',
    'images_reuse_filename': True,
    'object_resizing': True,  # ✅ Rasmlar hajmini o'zgartirishni yoqish
    'image_advtab': True,  # ✅ Rasm tahrirlash oynasida ilg‘or tabni qo‘shish
}
