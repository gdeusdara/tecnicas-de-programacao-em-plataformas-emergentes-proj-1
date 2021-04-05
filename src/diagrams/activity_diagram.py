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

    def add_source_qtd(self):
        self.source_qtd=self.source_qtd+1
    
    def add_target_qtd(self):
        self.source_qtd=self.target_qtd+1

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

        self.has_start_node=False
        self.has_final_node=False

        self.elements=[]
        self.transitions=[]

        for element in diagram["ActivityDiagramElements"]:
            if element["type"] == "StartNode":
              if not self.has_start_node:
                  self.elements.append(StartNode(element["name"]))
                  self.has_start_node=True
              else:
                  raise Exception("ActivityDiagramRuleException")

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
                self.has_final_node=True

        if not self.has_start_node:
            raise Exception("ActivityDiagramRuleException")
            
        if not self.has_final_node:
            raise Exception("ActivityDiagramRuleException")

        for transition in diagram["ActivityDiagramTransitions"]:
            node=Transition(transition["name"], transition["prob"], transition["source"], transition["target"])

            # node for source
            match_node, index = self.search(node.source)
            if match_node == None:
                raise Exception("ActivityDiagramRuleException")
            
            if match_node.has_max_source and match_node.max_source == match_node.source_qtd:
                raise Exception("ActivityDiagramRuleException")
            
            match_node.add_source_qtd()
            self.elements[index] = match_node

            # node for target
            match_node, index = self.search(node.target)
            if match_node == None:
                raise Exception("ActivityDiagramRuleException")
            
            if match_node.has_max_target and match_node.max_target == match_node.target_qtd:
                raise Exception("ActivityDiagramRuleException")
            
            match_node.add_target_qtd()
            self.elements[index] = match_node



            self.transitions.append(node)

    def search(self, name):
        for i in range(len(self.elements)):
            if self.elements[i].name == name:
                return self.elements[i], i
 
        return None, 0

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
