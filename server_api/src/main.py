from typing import Union;
from util import OntologyReader;

from fastapi import FastAPI

app = FastAPI();

ontology = OntologyReader();
[synonyms_and_biblical_references, scenarios_to_synonyms_and_biblical_references_index_map] = ontology.clean_and_prepare_ontology_data();
scenarios = list(scenarios_to_synonyms_and_biblical_references_index_map.keys());

del ontology;

print(synonyms_and_biblical_references);
print(scenarios_to_synonyms_and_biblical_references_index_map);
print(scenarios);

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/semantic/web/biblical-ontology/real-life-scenario/search/{scenario_keyword}")
def search_keyword(scenario_keyword: str):

    if ((not synonyms_and_biblical_references) or (not synonyms_and_biblical_references) or (not scenarios)): 
        return {"status": 404, "msg": "Can not currently respond to requests"}

    scenario_keyword = scenario_keyword.lower();

    try:
        # Will fail if search_keyword is not in ontology.
        # scenarios.index(scenario_keyword);
        ontology_information_index = scenarios_to_synonyms_and_biblical_references_index_map[scenario_keyword];

        [biblical_references, synonyms] =  synonyms_and_biblical_references[ontology_information_index];

        # synonyms.remove(scenario_keyword);

        response = {
            "status": 200,
            "search_term": scenario_keyword,
            "synonyms": synonyms,
            "biblical_references": biblical_references
        };

        return response;
    except Exception as err:
        return {"status": 404, "msg": "Information not found", "search_term": search_keyword};
