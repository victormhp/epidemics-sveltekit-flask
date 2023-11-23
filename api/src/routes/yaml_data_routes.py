import yaml
import networkx as nx
from flask import Blueprint, request, jsonify
from src.utils.generate_charts import get_model_data

main = Blueprint("yaml_blueprint", __name__)


@main.route("/", methods=["POST"])
def generate_chart_from_yaml():
    if request.method == "POST":
        files = request.files
        zoom = True if "zoom" in request.form else False

        # Default network, in case no graphml file is provided
        N = 10**5
        G = nx.barabasi_albert_graph(N, 4)

        if "graphml" in files and files["graphml"]:
            graphml_file = files["graphml"]
            G = nx.read_graphml(graphml_file)

        yaml_file = files["yaml"]
        if yaml_file:
            file_content = yaml_file.read()

            try:
                data = yaml.safe_load(file_content)

                if data is not None:
                    # Get and parse data
                    model = data["model"]
                    states = data["states"]
                    tau = float(data["transmissionRate"])
                    gamma = float(data["recoveryRate"])
                    rho = float(data["fractionInfected"])
                    data["zoom"] = zoom

                    model_data = get_model_data(G, model, states, tau, gamma, rho, zoom)

                    response = jsonify({"inputs": data, "positions": model_data})
                    return response
                else:
                    return jsonify({"error": "Invalid YAML file"})
            except yaml.YAMLError as e:
                return jsonify({"error": "YAML parsing error: " + str(e)}), 400
        else:
            response = jsonify({"error": "No file provided"}), 400
            return response
