from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from salary.forms import SalaryForm


class salaryTop(TemplateView):

    template_name = "salary/salaryInfo.html"

    def get_context_data(self, **kwargs):

        context = super(salaryTop, self).get_context_data(**kwargs)

        return context




class salaryInputView(FormView):


    template_name = "salary/salaryInput.html"
    form_class = SalaryForm
    success_url = ""

    def get_context_data(self, **kwargs):
        
        context = super(salaryInputView, self).get_context_data(**kwargs)

        return context
        







