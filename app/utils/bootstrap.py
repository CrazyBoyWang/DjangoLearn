from django import forms


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():  # 如果不想增加某个插件可以通过if来判断
            if field.widget.attrs:
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}
            else:
                print(name, field)
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}  # 定义插件方法
