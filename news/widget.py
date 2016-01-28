from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.contrib import admin
from django import forms
from django.forms.widgets import flatatt
from django.utils.encoding import smart_unicode
from django.utils.html import escape
# from django.utils import simplejson
from json import *

class MarkItUpWidget(forms.Textarea):
    class Media:
        js = (
            '../media/js/jquery-1.8.0.min.js',
            '../media/js/markitup/jquery.markitup.js',
            # '../media/js/markitup/sets/markdown/set.js',
            '../media/js/markitup/markItUp_init.js',
        )
        css = {
            'screen': (
                '../media/js/markitup/skins/markitup/style.css',
                '../media/js/markitup/sets/custom/style.css',
            )
        }


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150px" height="150px" /></a>' % \
                          (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


# class TinyMCEWidget(forms.Textarea):
#     """
#     TinyMCE widget. requires you include tiny_mce_src.js in your template
#     you can customize the mce_settings by overwriting instance mce_settings,
#     or add extra options using update_settings
#     """ 
#     class Media:
#         js = (
#             '../media/js/jquery-1.8.0.min.js',
#             '../media/js/tinymce/tinymce.min.js',
#             'media/js/tinymce/themes/simple/theme.min.js',
#         )

#     mce_settings = dict(
#         mode = "exact",
#         theme = "simple",
#         theme_advanced_toolbar_location = "top",
#         theme_advanced_toolbar_align = "center",
#     )    
             
#     def update_settings(self, custom):
#         return_dict = self.mce_settings.copy()
#         return_dict.update(custom)
#         return return_dict
    
#     def render(self, name, value, attrs=None):
#         if value is None: value = ''
#         value = smart_unicode(value)
#         final_attrs = self.build_attrs(attrs, name=name)
                   
#         self.mce_settings['elements'] = "id_%s" % name
#         mce_json = JSONEncoder().encode(self.mce_settings)
        
#         return mark_safe(u'<textarea%s>%s</textarea> <script type="text/javascript">\
#                 tinyMCE.init(%s)</script>' % (flatatt(final_attrs), escape(value), mce_json))