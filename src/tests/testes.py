import unittest
import pytest
from parameterized import parameterized

import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
from diagrams.activity_diagram import Node, StartNode, Activity, DecisionNode, MergeNode, Transition
from diagrams.sequence_diagrams import SequenceElement, Fragment, Lifeline, SequenceDiagrams, SequenceDiagram
import index

class TestProject:
    def test_falsificacao(self):
        entrada = "<ActivityDiagram name='nome_diagrama'>"
        saida = "</ActivityDiagram>"
        xml = entrada + saida
        assert (entrada == "<ActivityDiagram name='nome_diagrama'>" )
        assert (saida == "</ActivityDiagram>")
        assert (xml == "<ActivityDiagram name='nome_diagrama'></ActivityDiagram>")

    def test_dict(self):
        assert type(index.dict_activity_diagram) is dict

# testes diagrama de atividades
    def test_node(self):
        node = Node("node 1")
        assert(node.name == "node 1")
        assert(node.type == '')
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_source == 0)
        assert(node.max_target == 0)
        assert(node.has_max_source == False)
        assert(node.has_max_target == False)
    
    def test_node_2(self):
        node = Node("node 2")
        assert(node.name == "node 2")
        assert(node.type == '')
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_source == 0)
        assert(node.max_target == 0)
        assert(node.has_max_source == False)
        assert(node.has_max_target == False)

    def test_add_source_qtd(self):
        node = Node("node 1")
        assert(node.source_qtd == 0)
        
    def test_add_target_qtd(self):
        node = Node("node 1")
        assert(node.target_qtd == 0)

    def test_transition(self):
        transition = Transition("transition name", 1, "source name", "target name")
        assert(transition.name == "transition name")
        assert(transition.prob == 1)
        assert(transition.source == "source name")
        assert(transition.target == "target name")

    def test_transition_2(self):
        transition = Transition("transition name 2", 1, "source name 2", "target name 2")
        assert(transition.name == "transition name 2")
        assert(transition.prob == 1)
        assert(transition.source == "source name 2")
        assert(transition.target == "target name 2")



#testes diagrama de sequencia
    def test_sequence_element(self):
        sequenceElement = SequenceElement("sequence element name")
        assert(sequenceElement.name == "sequence element name")
        assert(sequenceElement.type == '')

    def test_sequence_element_2(self):
        sequenceElement = SequenceElement("sequence element name 2")
        assert(sequenceElement.name == "sequence element name 2")
        assert(sequenceElement.type == '')

    def test_fragment(self):
        fragment = Fragment("fragment name", "representation")
        assert(fragment.name == "fragment name")
        assert(fragment.representedBy == "representation")

    def test_fragment_2(self):
        fragment = Fragment("fragment name 2", "representation 2")
        assert(fragment.name == "fragment name 2")
        assert(fragment.representedBy == "representation 2")

    def test_lifeline(self):
        lifeline = Lifeline("lifeline")
        assert(lifeline.name == "lifeline")

    def test_lifeline_2(self):
        lifeline = Lifeline("lifeline 2")
        assert(lifeline.name == "lifeline 2")

    def test_sequence_diagram(self):
        sequenceDiagram = SequenceDiagram("sequence diagram name", "guard condition", "elements")
        assert(sequenceDiagram.name == "sequence diagram name")
        assert(sequenceDiagram.guard_condition == "guard condition")
        assert(sequenceDiagram.elements == "elements")

    def test_sequence_diagram_2(self):
        sequenceDiagram = SequenceDiagram("sequence diagram name 2", "guard condition 2", "elements 2")
        assert(sequenceDiagram.name == "sequence diagram name 2")
        assert(sequenceDiagram.guard_condition == "guard condition 2")
        assert(sequenceDiagram.elements == "elements 2")

    def test_file_exist(self):
        file = os.path.exists("diagrams.xml")
        assert(file)

  
        