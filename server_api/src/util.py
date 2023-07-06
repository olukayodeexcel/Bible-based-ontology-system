
# Search Keyword and return references.

from typing import NewType;
from owlready2 import *
from config import *;

Biblical_References = NewType('Biblical_Reference_List', dict['bookref': str, 'book': str, 'chapter': str, 'verse': str]);

class OntologyReader():

    

    def __init__(self) -> None:
       self.ontology = self.load_ontology_file();
       if (self.ontology == None): raise FileNotFoundError;


    def load_ontology_file(self):
        ontology_filepath = ontology_filename;
        ontology = get_ontology(ontology_filepath).load();
        if (type(ontology) is not Ontology): 
            print("[X] -> Error loading file ... ");
            return None;
        return ontology;





    def get_biblical_reference(self, ontology_biblical_refs: list[Ontology]) -> list[Biblical_References]:
        biblical_references: list[Biblical_References] = [];
        for ontology_biblical_ref in ontology_biblical_refs:

            biblical_reference_classes = ontology_biblical_ref.ancestors();
            biblical_reference_classes = set([str(reference.name) for reference in biblical_reference_classes]);
            biblical_reference_classes: set = biblical_reference_classes - biblical_ontology_biblical_references_junk_ancestor_set;

            verse = "";
            if (len(biblical_reference_classes) == 3):
                biblical_reference_classes.discard(ontology_biblical_ref.name);
                verse = ontology_biblical_ref.name.lower().split("vs")[1] or '';


            [biblical_ref_1, biblical_ref_2] = biblical_reference_classes;

            if (biblical_ref_1[-1].isdigit()):
                chapter = biblical_ref_1.split("CH")[1] or '';
                book = biblical_ref_2;
            else:
                chapter = biblical_ref_2.split("CH")[1] or '';
                book = biblical_ref_1;

            if (verse): bookref = book + " " + chapter + " vs " + verse;
            else: bookref = book + " " + chapter;

            biblical_references.append({'bookref':bookref, 'book': book, 'chapter': chapter, 'verse': verse});

        return biblical_references;





    def clean_and_prepare_ontology_data(self) -> tuple[list[Biblical_References],  dict[str: int]]:
        try:

            all_scenario_keywords = set([]);
            synonyms_and_biblical_references = [];
            scenarios_to_biblical_reference_index_map = {};

            # [canBeAccessedExo20, canBeGottenPsalmmat10, canBeGottenPsalm37, canBeLocatedDeu11, canBeObtained1sam17, canBeReferenced1thes5]
            ontology_object_properties = list(self.ontology.object_properties());
            for object_property in ontology_object_properties:

                if (len(object_property.domain) == 0 ): continue;

                real_life_scenario_class = object_property.domain[0];
                biblical_references = [bible_reference for bible_reference in object_property.range];

                # Returns all subclasses (including protege's "anonymous" subclasses).
                ancestors = list(real_life_scenario_class.ancestors());
                scenario_keywords = set( [ancestor.name for ancestor in ancestors] );
                scenario_keywords = scenario_keywords - biblical_ontology_real_life_scenario_junk_ancestor_set;
                scenario_keywords = [keyword.lower() for keyword in scenario_keywords];
                # scenario_keywords = list(scenario_keywords);
                all_scenario_keywords.update(scenario_keywords);

                references = self.get_biblical_reference(ontology_biblical_refs=biblical_references);

                # print(references);

                synonyms_and_biblical_references.append([references, scenario_keywords]);
                scenarios_to_biblical_reference_index_map[scenario_keywords[0]] = len(synonyms_and_biblical_references) - 1;
                scenarios_to_biblical_reference_index_map[scenario_keywords[1]] = len(synonyms_and_biblical_references) - 1;

            del ontology_object_properties;

            return (synonyms_and_biblical_references, scenarios_to_biblical_reference_index_map);



        except AttributeError as err:
            print('[X] Error:   Error loading ontology file ... ', err)
        except ValueError as err:
            print('[X] Error:   "scenario_class" not found in "ancestors" list ... ', err);


# clean_and_prepare_ontology_data();
n = OntologyReader();
