from django import forms

from .models import Product, Comment, Question, Answer


# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.TextInput()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "images"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
            if isinstance(field, forms.CharField):
                print(field.label, type(field.label))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
            if isinstance(field, forms.CharField):
                print(field.label, type(field.label))


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "header", "body"
        widgets = {"product": forms.HiddenInput()}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("body",)
        widgets = {"question": forms.HiddenInput()}
