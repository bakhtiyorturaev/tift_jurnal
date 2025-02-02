# TINYMCE_DEFAULT_CONFIG = {
#     'height': 360,
#     'width': 800,
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 20,
#     'selector': 'textarea',
#     'theme': 'silver',
#     'plugins': '''
#         save link image media preview codesample
#         table code lists fullscreen  insertdatetime  nonbreaking
#         directionality searchreplace wordcount visualblocks
#         visualchars code fullscreen autolink lists  charmap
#         anchor pagebreak
#     ''',
#     'toolbar1': '''
#         fullscreen preview bold italic underline | fontselect,
#         fontsizeselect  | forecolor backcolor | alignleft alignright |
#         aligncenter alignjustify | indent outdent | bullist numlist table |
#         | link image media | codesample |
#     ''',
#     'toolbar2': '''
#         visualblocks visualchars |
#         charmap hr pagebreak nonbreaking anchor |  code |
#     ''',
#     'contextmenu': 'formats | link image',
#     'menubar': True,
#     'statusbar': True,
# }




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
