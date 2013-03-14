from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from Products.Archetypes import atapi
from Products.ATContentTypes.interfaces import IATContentType
from zope.interface import Interface
from five import grok
from reddplusid.attachments.interfaces import IProductSpecific
from reddplusid.attachments import MessageFactory as _
from Products.validation import V_REQUIRED

# Visit http://pypi.python.org/pypi/archetypes.schemaextender for full 
# documentation on writing extenders

class ExtensionStringField(ExtensionField, atapi.FileField):
    pass

class AttachmentsExtender(grok.Adapter):

    # This applies to all AT Content Types, change this to
    # the specific content type interface you want to extend
    grok.context(IATContentType)

    grok.implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    grok.provides(IOrderableSchemaExtender)

    layer = IProductSpecific

    fields = [
        # add your extension fields here
        ExtensionFileField('attachment1', required=False,
            storage=atapi.AttributeStorage(),
            languageIndependent=True,
            widget=atapi.FileField._properties['widget'](
                label=_(u'Attachment 1')
            ),
            validators=(('isNonEmptyFile', V_REQUIRED),
                      ('checkFileMaxSize', V_REQUIRED)),
        ),
        ExtensionFileField('attachment2', required=False,
            storage=atapi.AttributeStorage(),
            languageIndependent=True,
            widget=atapi.FileField._properties['widget'](
                label=_(u'Attachment 2')
            ),
            validators=(('isNonEmptyFile', V_REQUIRED),
                      ('checkFileMaxSize', V_REQUIRED)),
        ),

        ExtensionFileField('attachment3', required=False,
            storage=atapi.AttributeStorage(),
            languageIndependent=True,
            widget=atapi.FileField._properties['widget'](
                label=_(u'Attachment 3')
            ),
            validators=(('isNonEmptyFile', V_REQUIRED),
                      ('checkFileMaxSize', V_REQUIRED)),
        ),
        ExtensionFileField('attachment4', required=False,
            storage=atapi.AttributeStorage(),
            languageIndependent=True,
            widget=atapi.FileField._properties['widget'](
                label=_(u'Attachment 4')
            ),
            validators=(('isNonEmptyFile', V_REQUIRED),
                      ('checkFileMaxSize', V_REQUIRED)),
        ),
        ExtensionFileField('attachment5', required=False,
            storage=atapi.AttributeStorage(),
            languageIndependent=True,
            widget=atapi.FileField._properties['widget'](
                label=_(u'Attachment 5')
            ),
            validators=(('isNonEmptyFile', V_REQUIRED),
                      ('checkFileMaxSize', V_REQUIRED)),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, schematas):
        # you may reorder the fields in the schemata here
        return schematas
