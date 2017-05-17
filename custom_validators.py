from wtforms.validators import ValidationError

class Options(object):
    # validator that checks field uniqueness
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'Please enter at least two options'
        self.message = message

    def __call__(self, form, field):
        if len(field.data.split(',')) < 2:
            raise ValidationError(self.message)

class Unique(object):
    # validator that checks field uniqueness
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'Username is already taken'
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)
