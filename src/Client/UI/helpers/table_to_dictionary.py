from rhythmic.general import faultReturnHandler;

@faultReturnHandler
def transformModelsTable(single_raw):
    """
    transformModelsTable(single_raw)
    transforms a row gotten via SQL request, to a dictionary
    """
    
    transformed = \
    {
        "id": single_raw[0],
        "name": single_raw[1],
        "path": single_raw[2],
        "version": single_raw[3],
        "timestamp": single_raw[4],
        "deploy_destination": single_raw[5],
        "descrtiption": single_raw[6],
        "metadata": single_raw[7]
    };

    return transformed;