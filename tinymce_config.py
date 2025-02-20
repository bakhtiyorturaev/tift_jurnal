
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 800,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
        advlist autolink lists link charmap anchor preview wordcount
    ''',
    'toolbar1': '''
        undo redo | bold italic underline | fontselect,
        fontsizeselect | forecolor backcolor | alignleft alignright |
        aligncenter alignjustify | indent outdent | bullist numlist |
        link | preview
    ''',
    'toolbar2': '''
        visualblocks visualchars |
        charmap anchor | code |
    ''',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'statusbar': True,
}
