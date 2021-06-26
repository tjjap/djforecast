from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput
from .models import Pipeline

# date picker
class DateInput(DateInput):
    input_type = 'date'


class PipelineForm(ModelForm):
    class Meta:
        model = Pipeline
        #fields = '__all__'
        fields = ['directorate', 'ambm', 'pid', 'client', 'project', 'onetime', 'nmonth', 'order_val', 'gpm', 'level', 'order_dd', 'bast_dd']
        widgets = {
            'order_dd': DateInput(),
            'bast_dd': DateInput()
        }
    
    # Clean method to validate multiple fields
    def clean(self):
        cleaned_data = super(PipelineForm, self).clean()
        data_bast = cleaned_data.get('bast_dd')
        data_order = cleaned_data.get('order_dd')

        if data_bast and data_order:
            if data_bast <= data_order:
                self.add_error('order_dd', 'Either change the SO Date or the BAST Date') #error message to related field
                self.add_error('bast_dd', ' Either change the BAST Date or the SO Date') #error message to related field
                raise ValidationError('You can\'t set BAST Date earlier than SO Date') #error message to non-field-errors

    # Clean_field method to validate a field
    '''
    def clean_bast_dd(self):
        data_bast = self.cleaned_data.get('bast_dd')
        data_order = self.cleaned_data.get('order_dd')

        if data_bast <= data_order:
            raise ValidationError('BAST Date must be later than SO Date')
        return data_bast
'''

    def clean_nmonth(self):
        data_onetime = self.cleaned_data.get('onetime')
        data_nmonth = self.cleaned_data.get('nmonth')

        if data_onetime and data_nmonth != 1:
            raise ValidationError("Should be 1")
        elif (not data_onetime) and (data_nmonth < 2):
            raise ValidationError("Should be >1")
        return data_nmonth


