from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from paypal.standard.forms import PayPalPaymentsForm

class ModifiedPaypalForm(PayPalPaymentsForm):
	amount = forms.DecimalField(decimal_places=2, label='Donasi', help_text='$')

	def clean(self):
		data = self.cleaned_data
		if data.get('amount')<Decimal('0'):
			self._errors['amount'] = ErrorList([
		        u'Please input correct amount.'])

		return data

	# def render(self):
	# 	return mark_safe(u"""<form action="%s" method="post">{% csrf_token %}
 #    	%s
 #    	<input type="image" src="%s" border="0" name="submit" alt="Buy it Now" />
	# 	</form>""" % (reverse('program_donate'), self.as_p(), self.get_image()))