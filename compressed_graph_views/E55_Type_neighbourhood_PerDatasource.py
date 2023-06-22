
datasources = ["Huma-Num - Nakala", "Huma-Num - Isidore", "PARTHENOS", "METASHARE", "Cultura Italia", "LRE MAP", "European Holocaust Research Infrastructure", "CENDARI", "CLARIN", "ARIADNE"] # orderd by size

    
# -------------------- OPTIONAL SETTINGS -------------------- 

# title
# defines the title of the whole set of queries
# OPTIONAL, if not set, timestamp will be used
title = ["E55_Type_neighbourhood_", datasources]


# description
# defines the textual and human-intended description of the purpose of these queries
# OPTIONAL, if not set, nothing will be used or displayed
description = ""


# output_destination
# defines where to save the results, input can be: 
# * a local path to a folder 
# * a URL for a google sheets document  
# * a URL for a google folder
# NOTE: On windows, folders in a path use backslashes, in such a case it is mandatory to attach a 'r' in front of the quotes, e.g. r"C:\Users\sresch\.."
# In the other cases the 'r' is simply ignored; thus best would be to always leave it there.
# OPTIONAL, if not set, folder of executed script will be used
output_destination = r"./E55_Type_neighbourhood/PerDatasource"


# output_format
# defines the format in which the result data shall be saved (currently available: csv, tsv, xml, json, xlsx)
# OPTIONAL, if not set, csv will be used
output_format = "csv"


# summary_sample_limit
# defines how many rows shall be displayed in the summary
# OPTIONAL, if not set, 5 will be used
summary_sample_limit = 100


# cooldown_between_queries
# defines how many seconds should be waited between execution of individual queries in order to prevent exhaustion of Google API due to too many writes per time-interval
# OPTIONAL, if not set, 0 will be used
cooldown_between_queries = 0


# write_empty_results
# Should tabs be created in a summary file for queries which did not return results? Possible values are python boolean values: True, False
# OPTIONAL, if not set, False will be used
write_empty_results = False


# -------------------- MANDATORY SETTINGS -------------------- 

# endpoint
# defines the SPARQL endpoint against which all the queries are run
# MANDATORY
# endpoint = "http://dbpedia.org/sparql"
endpoint = "https://virtuoso.parthenos.d4science.org/sparql"
# endpoint = "http://localhost:8890/sparql"
# endpoint = "https://parthenos-virtuoso.hephaistos.arz.oeaw.ac.at/sparql"

# queries
queries = [
    {
        "title" : [datasources, "_i -> ir"],
        "query" : [r"""

            select

            <i> as ?id_subject_group
            count( distinct ?i ) as ?subject_group_count

            ?i_p_ir as ?relation
            count(?i_p_ir) as ?relation_count

            <ir> as ?id_object_group
            count( distinct ?ir ) as ?object_group_count

            where {

                graph ?sourceGraph {
                
                    ?i ?i_p_ir ?ir .
                    
                    {
                        select distinct ?i where {
                            graph ?sourceGraph {                    
                                ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
                            }
                            graph <dnet:graph> {
                                ?sourceGraph <dnet:collectedFrom> ?api .
                                ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                            }
                        }
                    }                    
                }
                graph <dnet:graph> {
                    ?sourceGraph <dnet:collectedFrom> ?api .
                    ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                }
            }
            group by ?i_p_ir
        """]
    },
    {
        "title": [datasources, "_il -> i"],
        "query": [r"""

            select

            <il> as ?id_subject_group
            count( distinct ?il ) as ?subject_group_count

            ?il_p_i as ?relation
            count( ?il_p_i ) as ?relation_count

            <i> as ?id_object_group
            count( distinct ?i ) as ?object_group_count

            where {

                graph ?sourceGraph {

                    ?il ?il_p_i ?i .

                    {
                        select distinct ?i where {
                            graph ?sourceGraph {
                                ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
                            }
                            graph <dnet:graph> {
                                ?sourceGraph <dnet:collectedFrom> ?api .
                                ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                            }
                        }
                    }
                }
                graph <dnet:graph> {
                    ?sourceGraph <dnet:collectedFrom> ?api .
                    ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                }
            }
            group by ?il_p_i
        """]
    },
    {
        "title": [datasources, "_ir -> irr"],
        "query": [r"""

            select

            <ir> as ?id_subject_group
            count( distinct ?ir ) as ?subject_group_count

            ?ir_p_irr as ?relation
            count( ?ir_p_irr ) as ?relation_count

            <irr> as ?id_object_group
            count( distinct ?irr ) as ?object_group_count

            where {

                graph ?sourceGraph {

                    ?ir ?ir_p_irr ?irr .

                    {
                        select distinct ?ir where {

                            graph ?sourceGraph {

                                ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .

                                ?i ?i_p_ir ?ir .
                            }
                            graph <dnet:graph> {
                                ?sourceGraph <dnet:collectedFrom> ?api .
                                ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                            }
                        }
                    }
                }
                graph <dnet:graph> {
                    ?sourceGraph <dnet:collectedFrom> ?api .
                    ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                }
            }
            group by ?ir_p_irr
        """]
    },
    {
        "title": [datasources, "_irl -> ir"],
        "query": [r"""

            select

            <irl> as ?id_subject_group
            count( distinct ?irl ) as ?subject_group_count

            ?irl_p_ir as ?relation
            count( ?irl_p_ir ) as ?relation_count

            <ir> as ?id_object_group
            count( distinct ?ir ) as ?object_group_count

            where {

                graph ?sourceGraph {

                    ?irl ?irl_p_ir ?ir .
                    minus {
                        ?irl <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
                        ?irl ?irl_p_ir ?ir .
                    }

                    {
                        select distinct ?ir where {
                            graph ?sourceGraph {

                                ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .

                                ?i ?i_p_ir ?ir .
                            }
                            graph <dnet:graph> {
                                ?sourceGraph <dnet:collectedFrom> ?api .
                                ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                            }
                        }
                    }
                }
                graph <dnet:graph> {
                    ?sourceGraph <dnet:collectedFrom> ?api .
                    ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                }
            }
            group by ?irl_p_ir

        """]
    },
    {
        "title": "il -> ilr",
        "query": [r"""

            select

            <il> as ?id_subject_group
            count( distinct ?il ) as ?subject_group_count

            ?il_p_ilr as ?relation
            count( ?il_p_ilr ) as ?relation_count

            <ilr> as ?id_object_group
            count( distinct ?ilr ) as ?object_group_count

            where {
                graph ?sourceGraph {
                
                    ?il ?il_p_ilr ?ilr .
                    minus {
                        ?il ?il_p_ilr ?i .
                        ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
                    }
                        
                    {
                        select distinct ?il where {
                            graph ?sourceGraph {

                                ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
    
                                ?il ?il_p_i ?i .
                            }
                            graph <dnet:graph> {
                                ?sourceGraph <dnet:collectedFrom> ?api .
                                ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                            }
                        }
                    }
                }
                graph <dnet:graph> {
                    ?sourceGraph <dnet:collectedFrom> ?api .
                    ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                }
            }
            group by ?il_p_ilr
        """]
    },
    {
        "title": "ill -> il",
        "query": [r"""

            select

            <ill> as ?id_subject_group
            count( distinct ?ill ) as ?subject_group_count

            ?ill_p_il as ?relation
            count( ?ill_p_il ) as ?relation_count

            <il> as ?id_object_group
            count( distinct ?il ) as ?object_group_count

            where {
                graph ?sourceGraph {
                
                    ?ill ?ill_p_il ?il .
                    
                    {
                        select distinct ?il where {
                            graph ?sourceGraph {
                                ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
    
                                ?il ?il_p_i ?i .
                            }
                            graph <dnet:graph> {
                                ?sourceGraph <dnet:collectedFrom> ?api .
                                ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                            }                                
                        }
                    }
                }
                graph <dnet:graph> {
                    ?sourceGraph <dnet:collectedFrom> ?api .
                    ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
                }
            }
            group by ?ill_p_il
        """]
    },










    # {
    #     "title" : "",
    #     "query" : r"""
    #
    #         select
    #         ?
    #         count( distinct ?) as ?count
    #         where {
    #
    #             graph ?sourceGraph {
    #
    #                 ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
    #
    #             }
    #             graph <dnet:graph> {
    #                 ?sourceGraph <dnet:collectedFrom> ?api .
    #                 ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
    #             }
    #         }
    #         group by ?
    #
    #     """
    # },
    # {
    #     "title" : "",
    #     "query" : r"""
    #
    #         select
    #         ?
    #         count( distinct ?)
    #         where {
    #
    #             graph ?sourceGraph {
    #
    #                 ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
    #
    #             }
    #             graph <dnet:graph> {
    #                 ?sourceGraph <dnet:collectedFrom> ?api .
    #                 ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
    #             }
    #         }
    #         group by ?
    #
    #     """
    # },
    # {
    #     "title" : "",
    #     "query" : r"""
    #
    #         select
    #         ?
    #         count( distinct ?)
    #         where {
    #
    #             graph ?sourceGraph {
    #
    #                 ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
    #
    #             }
    #             graph <dnet:graph> {
    #                 ?sourceGraph <dnet:collectedFrom> ?api .
    #                 ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
    #             }
    #         }
    #         group by ?
    #
    #     """
    # },
    # {
    #     "title" : "",
    #     "query" : r"""
    #
    #         select
    #         ?
    #         count( distinct ?)
    #         where {
    #
    #             graph ?sourceGraph {
    #
    #                 ?i <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E55_Type> .
    #
    #             }
    #             graph <dnet:graph> {
    #                 ?sourceGraph <dnet:collectedFrom> ?api .
    #                 ?api <dnet:isApiOf> '""", datasources, r"""'^^<http://www.w3.org/2001/XMLSchema#string>
    #             }
    #         }
    #         group by ?
    #
    #     """
    # },
]
# defines the set of queries to be run.
# MANDATAORY

# Each query is itself encoded as a python dictionary, and together these dictionaries are collected in a python list. 
# Beginner's note on such syntax as follows:
# * the set of queries is enclosed by '[' and ']'
# * individual queries are enclosed by '{' and '},'
# * All elements of a query (title, description, query) need to be defined using quotes as well as their contents, and both need to be separated by ':'
# * All elements of a query (title, description, query) need to be separated from each other using quotes ','
# * The content of a query needs to be defined using triple quotes, e.g. """ SELECT * WHERE .... """
# * Any indentation (tabs or spaces) do not influence the queries-syntax, they are merely syntactic sugar.



# --------------- CUSTOM POST-PROCESSING METHOD --------------- 
'''
The method 'custom_post_processing(results)' is a stump for custom post processing which is always called if present and to which
result data from the query execution is passed. This way you can implement your own post-processing steps there.

The incoming 'results' argument is a list, where each list-element is a dictionary represting all data of a query.

This dictionary has the following keys and respective values:

* most likely to be needed are these two keys and values:
'query_title' - title of an individual query, as defined above.
'results_matrix' - the result data organized as a two dimensional list, where the first row contains the headers. 
This value is what you would most likely need to post process the result data.  

* other than these two, each query dictionary also contains data from and for querPy, which might be of use:
'query_description' - description of an individual query, as defined above.
'query_text' - the sparql query itself.
'results_execution_duration' - the duration it took to run the sparql query.
'results_lines_count' - the number of lines the sparql query produced at the triplestore.
'results_raw' - the result data in the specified format, encapsulated by its respective python class (e.g. a python json object).
'query_for_count' - an infered query from the original query, is used to get number of result lines at the triplestore.

As an example to print the raw data from the second query defined above, write:
print(results[1]['results_matrix'])
'''

# UNCOMMENT THE FOLLOWING LINES FOR A QUICKSTART:
def custom_post_processing(results):

    run_id = "E55_PerDatasource_1"

    def main(results):

        persist_to_neo4j(results)


    def persist_to_neo4j(results):


        results_matrix = []
        for result in results:
            results_matrix_tmp = result['results_matrix'][1:]
            if len(results_matrix_tmp) > 0:
                results_matrix_tmp = clean_of_PE_prefixes(results_matrix_tmp)
                results_matrix.extend(results_matrix_tmp)



        from neo4j.v1 import GraphDatabase

        # results_matrix = [
        #     ["i", 2, "a_p_r", 4, "ir", 4],
        #     ["i", 2, "a_p_r2", 2, "ir", 4],
        #     ["il", 1, "l_p_a", 1, "i", 1],
        #     ["ir", 1, "r_p_rr", 2, "irr", 2],
        #     ["irl", 1, "rl_p_r", 1, "ir", 1]
        # ]
        # print(results_matrix)

        driver = GraphDatabase.driver("bolt://localhost", auth=("neo4j","password"))

        datasource_string = results[0]['query_title']
        try:
            datasource_string = datasource_string.split(". ", 1)[1].split("_")[0]
        except IndexError:
            pass


        with driver.session() as session:

            # session.run("MATCH (n) DETACH DELETE (n)")

            for row in results_matrix:

                session.run(
                    "MERGE (n1:`" + run_id + "` {id: '" + row[0] + "', datasource: '" + datasource_string + "'})\n" +
                    " ON CREATE SET n1.s = " + str(row[1]) + ", n1.o = 0 \n" +
                    " ON MATCH SET n1.s = n1.s + " + str(row[1])
                )

                session.run(
                    "MERGE (n2:`" + run_id + "` {id: '" + row[4] + "', datasource: '" + datasource_string + "'})\n" +
                    "ON CREATE SET n2.o = " + str(row[5]) + ", n2.s = 0 \n" +
                    "ON MATCH SET n2.o = n2.o + " + str(row[5])
                )

                session.run(
                    "MATCH (n1:`" + run_id + "` {id: '" + row[0] + "', datasource: '" + datasource_string + "'})\n" +
                    "MATCH (n2:`" + run_id + "` {id: '" + row[4] + "', datasource: '" + datasource_string + "'})\n" +
                    "CREATE (n1)-[:`" + run_id + "` { label: '" + row[2] + " (" + str(row[3]) + ")'}]->(n2)"
                )

            session.run(
                "MATCH (n:`" + run_id + "`)\n" +
                "SET n.label = 'o(' + n.o + '), s(' + n.s + ')'"
            )

            session.close()


    def clean_of_PE_prefixes(value):

        def clean_string_of_PE_prefixes(value_string):
            return value_string \
                .replace('http://www.cidoc-crm.org/cidoc-crm/', '') \
                .replace('CRMsci/', '') \
                .replace('http://parthenos.d4science.org/CRMext/CRMpe.rdfs/', '') \
                .replace('http://www.ics.forth.gr/isl/CRMext/CRMdig.rdfs/', '') \
                .replace('http://www.w3.org/2000/01/rdf-schema#', 'rdf:') \
                .replace('http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'rdf:')

        if isinstance(value, str):
            return clean_string_of_PE_prefixes(value)
        elif isinstance(value, list):
            for i in range(0, len(value)):
                if ( isinstance(value[i], str) or isinstance(value[i], list)):
                    value[i] = clean_of_PE_prefixes(value[i])
            return value
        else:
            raise Exception('Only lists or string values can be cleaned.')


    main(results)

