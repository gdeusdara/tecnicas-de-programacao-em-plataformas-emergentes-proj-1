class SequenceElement:
    def __init__(self, name):
        self.name=name
        self.type=''

class FragmentReference(SequenceElement):
    def __init__(self, name):
      super().__init__(name)
      self.type='Fragment'

class Message(SequenceElement):
    def __init__(self, name, message_type, prob, source, target):
      super().__init__(name)
      self.type='Message'
      self.message_type=message_type
      self.prob=prob
      self.source=source
      self.target=target

class Fragment:
    def __init__(self, name, representedBy):
        self.name=name
        self.representedBy=representedBy

class Lifeline:
    def __init__(self, name):
        self.name=name

class SequenceDiagram:
    def __init__(self, name, guard_condition, elements):
        self.name=name
        self.guard_condition=guard_condition
        self.elements=elements

class SequenceDiagrams():
    def __init__(self, diagram):
        self.lifelines=[]
        self.fragments=[]
        self.diagrams=[]

        for element in diagram["Lifelines"]:
            lifeline=Lifeline(element["name"])
            self.lifelines.append(lifeline)

        for element in diagram["Fagments"]:
            fragment=Fragment(element["name"], element["representedBy"])
            self.fragments.append(fragment)

        for sequence_diagram in diagram["SequenceDiagrams"]:

            elements=[]
            for element in sequence_diagram["elements"]:

                if element["type"] == "Fragment":
                    node=FragmentReference(element["name"])
                    elements.append(node)

                if element["type"] == "Message":
                    node=Message(element["name"], element["message_type"], element["prob"], element["source"], element["target"])
                    elements.append(node)
            
            this_diagram=SequenceDiagram(sequence_diagram["name"], sequence_diagram["guard_condition"], elements)
            self.diagrams.append(this_diagram)


    def getXml(self):
        
        print('<SequenceDiagrams>')
        print('\t<Lifelines>')
        for lifeline in self.lifelines:
              print('\t\t<Lifeline name="{}" />'.format(lifeline.name))
        print('\t</Lifelines>')
    
        print('\t<Fragments>')
        for fragment in self.fragments:
            print('\t\t<Optional name="{}" representedBy="{}" />'.format(fragment.name, fragment.representedBy))
        print('\t</Fragments>')
        for diagram in self.diagrams:
            print('\t<SequenceDiagram name="{}" guardCondition="{}">'.format(diagram.name, diagram.guard_condition))
            for element in diagram.elements:
                if element.type == 'Message':   
                    print('\t\t<Message name="{}" prob="{}" source="{}" target="{}" />'.format(element.name, element.prob, element.source, element.target))
                else:
                    print('\t\t<Fragment name="{}" />'.format(element.name))

            print('\t</SequenceDiagram>')

