
# Search Keyword and return references.

from typing import NewType;
from owlready2 import *
from config import *;






def load_ontology_file():
    ontology_filepath = ontology_filename;
    ontology = get_ontology(ontology_filepath).load();
    if (type(ontology) is not Ontology): 
        print("[X] -> Error loading file ... ");
        return None;
    return ontology;



Biblical_References = NewType('Biblical_Reference_List', list[dict['bookref': str, 'book': str, 'chapter': str, 'verse': str]]);
# [1CRCH20_Vs4, 1_Chr_CH20, 1_Chronicles]
# [EXCH20_Vs4, Exo_CH20, Exodus]
def get_biblical_reference(ontology_biblical_refs: list[Ontology]) -> Biblical_References:
    print("<-> ========================================= <->")
    # biblical_references = [bible_reference for bible_reference in ontology_biblical_ref.range];
    biblical_references: Biblical_References = [];
    for ontology_biblical_ref in ontology_biblical_refs:
        print("\n", ontology_biblical_ref);
        biblical_reference_classes = ontology_biblical_ref.ancestors();
        biblical_reference_classes = set([str(reference.name) for reference in biblical_reference_classes]);
        biblical_reference_classes: set = biblical_reference_classes - biblical_ontology_biblical_references_junk_ancestor_set;
        print(biblical_reference_classes);

        verse = "";
        if (len(biblical_reference_classes) == 3):
            biblical_reference_classes.discard(ontology_biblical_ref.name);
            verse = ontology_biblical_ref.name.lower().split("vs")[1] or '';

        print(biblical_reference_classes);

        [biblical_ref_1, biblical_ref_2] = biblical_reference_classes;

        if (biblical_ref_1[-1].isdigit()):
            chapter = biblical_ref_1.split("CH")[1] or '';
            book = biblical_ref_2;
        else:
            chapter = biblical_ref_2.split("CH")[1] or '';
            book = biblical_ref_1;

        
        print(biblical_ref_1, biblical_ref_2);

        biblical_references.append({'bookref': f"{book} {chapter} {verse}", 'book': book, 'chapter': chapter, 'verse': verse});
        print(({'bookref': f"{book} {chapter} {verse}", 'book': book, 'chapter': chapter, 'verse': verse}));


    return biblical_references;

# real_life_scenario = ontology["Real_life_scenario"];
# ontology = load_ontology_file();

# # real_life_scenario = ontology.Real_life_scenario;
# # real_life_scenario_subclasses = list(real_life_scenario.subclasses());
# ontology_object_properties = list(ontology.object_properties());
# object_property = ontology_object_properties[0];
# object_property_ancestors = (ontology_object_properties[0].range);
# biblical_reference_classes = set([ancestor.name for ancestor in object_property_ancestors]);
# biblical_reference_classes: set = biblical_reference_classes - biblical_ontology_biblical_references_junk_ancestor_set;
# print(biblical_reference_classes);
# print(ontology_object_properties[0].range[0].ancestors());
# print(ontology.search(is_a=ontology["Exo_CH20"], subclass_of=ontology["Exo_CH20"]));
# print(get_biblical_reference(ontology_biblical_refs=object_property_ancestors));

# print((list(ontology.classes()))[0:50]);
# adultery = ontology["Supervision"];

# print(real_life_scenario.namespace);
# print(real_life_scenario_subclasses);
# print(dir(adultery), [str(x.name) for x in  [ c.ancestors() for c in real_life_scenario_subclasses ] ]);
# print(help(real_life_scenario_subclasses[0]));
# print(real_life_scenario_subclasses[0].get_equivalent_to());
# print(ontology.search(subclass_of=adultery));
# print((ontology_object_properties[0].domain[0].get_properties()));
# print();



def clean_and_prepare_ontology_data() -> dict['scenario_references': list[str]]:
    try:
        ontology = load_ontology_file();

        all_scenario_keywords = set([]);

        # [canBeAccessedExo20, canBeGottenPsalmmat10, canBeGottenPsalm37, canBeLocatedDeu11, canBeObtained1sam17, canBeReferenced1thes5]
        ontology_object_properties = list(ontology.object_properties());
        for object_property in ontology_object_properties:
            print('\n',object_property.name);
            if (len(object_property.domain) == 0 ): continue;

            real_life_scenario_class = object_property.domain[0];
            biblical_references = [bible_reference for bible_reference in object_property.range];

            # Returns all subclasses (including protege's "anonymous" subclasses).
            ancestors = list(real_life_scenario_class.ancestors());
            # print("Ancestors:", ancestors);
            # equivalent_scenario_class = set( [str(ancestor.name) for ancestor in ancestors].remove(str(real_life_scenario_class.name)) );
            scenario_keywords = set( [ancestor.name for ancestor in ancestors] );
            scenario_keywords = scenario_keywords - biblical_ontology_real_life_scenario_junk_ancestor_set;
            scenario_keywords = list(scenario_keywords);
            all_scenario_keywords.update(scenario_keywords);
            # all_scenario_keywords.extend(scenario_keywords);

            # We can alternatively derive the list from the "ObjectProperty" "domain" attribute which === scenario class.
            # print("<-> ", [real_life_scenario_class.name, equivalent_scenario_class], " - ", biblical_references);
            # print("<-> ", scenario_keywords, " - ", biblical_references);
            references = get_biblical_reference(ontology_biblical_refs=biblical_references);

            print(references);


    

    except AttributeError as err:
        print('[X] Error:   Error loading ontology file ... ', err)
    except ValueError as err:
        print('[X] Error:   "scenario_class" not found in "ancestors" list ... ', err);


clean_and_prepare_ontology_data();


clean_and_prepare_ontology_data();


def search_keyword(search_term: str):
    keyword = ontology[search_term];
    if (keyword == None): return {"status": 404, "msg": "Search Term Not Found"};

    pass;