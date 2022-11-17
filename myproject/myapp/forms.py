from django .forms import ModelForm
from .models import Feedback
from .models import Poll

class createpollform(ModelForm):
    class Meta:
        model=Poll
        fields=['question','option_one','option_two','option_three','option_four']
        
class createfeedback(ModelForm):
    class Meta:
        model=Feedback
        fields=['feedback']
        


