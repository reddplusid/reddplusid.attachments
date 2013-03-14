from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AttachmentsViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/attachmentsviewlet.pt')

    def available(self):
        for i in range(1,6):
            val = getattr(self.context, 'attachment%s' % i, None)
            if val and val.size:
                return True
        return False
