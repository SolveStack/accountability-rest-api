import inspect


class Choices(object):
    def list():
        list_of_attributes = list()
        for i in inspect.getmembers(__class__):
            if not i[0].startswith('_') and not inspect.isfunction(i[1]):
                list_of_attributes.append(i[1])

        return list_of_attributes

class PublishStatus(Choices):
    PUBLISHED = ("published", "Published")
    QA = ("qa", "QA")
    DRAFT = ("draft", "Draft")
