from django.contrib import admin
from school import models

admin.site.unregister(models.User)
for model in models.__dict__.values():
	if isinstance(model, models.models.base.ModelBase):
		admin.site.register(model)
