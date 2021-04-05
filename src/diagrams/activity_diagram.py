"""
dict_activity_diagram = {
  "name": "test"
  "ActivityDiagramElements": [
    {
        "type": "StartNode",
        "name": "nome do start node"
    },
    {
        "type": "Activity",
        "name": "nome da atividade"
    },
    {
        "type": "DecisionNode",
        "name": "nome do nodo de decisao"
    },
    {
        "type": "MergeNode",
        "name": "nome da atividade"
    },
    {
       "type": "FinalNode",
        "name": "nome do nodo final"
    },
  ],
  "ActivityDiagramTransitions": [
    {
      "name": "transition name",
      "prob": 1,
      "source": "node inicial",
      "target": "node final"
    }
  ]
}
"""

"""
<ActivityDiagram name=‘‘nome do diagrama’’>
  <ActivityDiagramElements>
    <StartNode name=‘‘nome do nodo inicial’’/>
    <Activity name=‘‘atividade 1’’/>
    <DecisionNode name=‘‘nome do nodo de decisao’’/>
    <Activity name=‘‘atividade 2’’/>
    <MergeNode name=‘‘nome do nodo de fusao’’/>
    <Activity name=‘‘atividade 3’’/>
    <FinalNode name=‘‘nome do nodo final’’/>
  </ActivityDiagramElements> 
  <ActivityDiagramTransitions>
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="atividade 1" target="atividade 2" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
    <Transition source="nome do nodo inicial" target="atividade 1" name=‘‘nome da transicao’’ prob="1" />
  </ActivityDiagramTransitions>
</ActivityDiagram>

<SequenceDiagrams>
  <Lifelines>
    <Lifeline name=‘‘nome da lifeline’’ />
    <Lifeline name=‘‘nome da lifeline’’
    <Lifeline name=‘‘nome da lifeline’’ />
  </Lifelines> /> 

  <Fragments>
    <Optional name=‘‘nome do fragmento’’ representedBy=‘‘nome do diagrama de sequencia’’/>
    <Optional name=‘‘nome do fragmento’’ representedBy=‘‘nome do diagrama de sequencia’’/>
    <Optional name=‘‘nome do fragmento’’ representedBy=‘‘nome do diagrama de sequencia’’/>
    ...
  </Fragments>

  <SequenceDiagram name=‘‘atividade 1’’>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Fragment name=‘‘nome do fragmento’’/>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    ...
  </SequenceDiagram>

  <SequenceDiagram name=‘‘atividade 2’’>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Fragment name=‘‘nome do fragmento’’/>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    ...
  </SequenceDiagram>

  <SequenceDiagram name=‘‘nome do diagrama’’>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    <Fragment name=‘‘nome do fragmento’’/>
    <Message name=‘‘nome da mensagem’’ prob=‘‘valor da probabilidade’’ source=‘‘nome da lifeline’’ target=‘‘nome da lifeline’’ />
    ...
  </SequenceDiagram>
"""

class Node:
    def __init__(self, name):
        self.name=name
        self.type=''
        self.source_qtd=0
        self.target_qtd=0
        self.max_source=0
        self.max_target=0
        self.has_max_source=False
        self.has_max_target=False

class StartNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.type='StartNode'
        self.has_max_target=True
        self.has_max_source=True
        self.max_source=1

class Activity(Node):
    def __init__(self, name):
        super().__init__(name)
        self.type='Activity'
        self.has_max_target=True
        self.max_target=1
        self.has_max_source=True
        self.max_source=1


class DecisionNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.type='DecisionNode'
        self.has_max_target=True
        self.max_target=1

class MergeNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.type='MergeNode'
        self.has_max_source=True
        self.max_source=1

class FinalNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.type='FinalNode'
        self.has_max_target=True
        self.has_max_source=True
        self.max_target=1

class Transition:
    def __init__(self, name, prob, source, target):
        super().__init__()
        self.name=name
        self.prob=prob
        self.target=target
        self.source=source


class ActivityDiagram:
    def __init__(self, diagram):
        self.name=diagram["name"]
        self.elements=[]
        self.transitions=[]

        for element in diagram["ActivityDiagramElements"]:
            if element["type"] == "StartNode":
                self.elements.append(StartNode(element["name"]))

            if element["type"] == "Activity":
                node=Activity(element["name"])
                self.elements.append(node)

            if element["type"] == "DecisionNode":
                node=DecisionNode(element["name"])
                self.elements.append(node)

            if element["type"] == "MergeNode":
                node=MergeNode(element["name"])
                self.elements.append(node)

            if element["type"] == "FinalNode":
                node=FinalNode(element["name"])
                self.elements.append(node)

        # if self.start_node == None:
        #     raise Exception("ActivityDiagramRuleException")
        # if len(self.final_node) == 0:
        #     raise Exception("ActivityDiagramRuleException")

        for transition in diagram["ActivityDiagramTransitions"]:
            node=Transition(transition["name"], transition["prob"], transition["source"], transition["target"])
            self.transitions.append(node)

    def getXml(self):
        
        print('<ActivityDiagram name="{}">'.format(self.name))
        print('\t<ActivityDiagramElements>')

        for element in self.elements:
            print('\t\t<{} name="{}"/>'.format(element.type, element.name))

        print('\t</ActivityDiagramElements>')
        print('\t<ActivityDiagramTransitions>')

        for transition in self.transitions:
            print('\t\t<Transition source="{}" target="{}" name="{}" prob="{}" />'.format(transition.source, transition.target, transition.name, transition.prob))

        print('\t</ActivityDiagramTransitions>')
        print('</ActivityDiagram>')
