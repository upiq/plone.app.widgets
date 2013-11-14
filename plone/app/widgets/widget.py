# -*- coding: utf-8 -*-

from plone.app.widgets.dx import AjaxSelectWidget
from plone.app.widgets.dx import RelatedItemsWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.widget import FieldWidget
from zope.interface import implementer


@implementer(IFieldWidget)
def RelatedItemsFieldWidget(field, request):
    widget = FieldWidget(field, AjaxSelectWidget(request))
    return widget


@implementer(IFieldWidget)
def MultiRelatedItemsFieldWidget(field, request):
    widget = FieldWidget(field, RelatedItemsWidget(request))
    return widget
