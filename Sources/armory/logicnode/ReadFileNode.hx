package armory.logicnode;

class ReadFileNode extends LogicNode {

	var data:String;

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run(from:Int) {
		// Relative or absolute path to file
		var file:String = inputs[1].get();

		// Load the file asynchronously
		iron.data.Data.getBlob(file, function(b:kha.Blob) {
			data = b.toString();
			runOutput(0);
		});
	}

	override function get(from:Int):Dynamic {
		return data;
	}
}
