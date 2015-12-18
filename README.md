# MNIST Web
MNIST digit recognizer website. Built with jQuery, Flask, numpy. Configuration can be made in config.json file. Live demo: https://digits-recognizer.herokuapp.com/


Config.json example:
```sh
{
	"port": 1234,
	"activationFunction": "Sigmoid",
	"layer1": "layer_1.json",
	"layer2": "layer_2.json",
	"train": "data.csv"
}
```

 - port : defines what port will be used for the website
 - activationFunction : what kind of activation function was used in neural network
 - layer1 : first layer of neural network (JSON format)
 - layer2 : second layer of neural network (JSON format)
 - train : if you click 'train' button in website, data will be written in this defined file (CSV format)

 To make neural network layers, this project was used: 
 https://github.com/evalkaz94/neural_network_py

### Please note that order of layers is IMPORTANT!