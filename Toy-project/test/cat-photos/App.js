import Nodes from "./Nodes.js";
import Breadcrumb from "./Breadcrumb.js";
import ImageView from "./ImageView.js";
import { request } from "./api.js";

export default function App($app) {
  this.state = {
    isRoot: false,
    nodes: [],
    depth: [],
    selectedFilePath: null,
  };

  const breadcrumb = new Breadcrumb({
    $app,
    initialState: this.state.depth,
  });

  const nodes = new Nodes({
    $app,
    initialState: {
      isRoot: this.state.isRoot,
      nodes: this.state.nodes,
    },
    onClick: async (node) => {
      try {
        if (node.type === "DIRECTORY") {
          const nextNodes = await request(node.id);
          this.setState({
            ...this.state,
            depth: [...this.state.depth, node],
            nodes: nextNodes,
          });
        } else if (node.type === "FILE") {
          this.setState({
            ...this.state,
            selectedFilePath: node.filePath,
          });
        }
      } catch (e) {
        new Error("failed onClick request");
      }
    },
  });

  const imageView = new ImageView({
    $app,
    initialState: this.state.selectedNodeImage,
  });

  this.setState = (nextState) => {
    this.state = nextState;
    breadcrumb.setState(this.state.depth);
    nodes.setState({
      isRoot: this.state.isRoot,
      nodes: this.state.nodes,
    });
    imageView.setState(this.state.selectedFilePath);
  };

  const init = async () => {
    console.log("hello");
    try {
      const rootNodes = await request();
      console.log(rootNodes);
      this.setState({
        ...this.state,
        isRoot: true,
        nodes: rootNodes,
      });
    } catch (e) {
      new Error(`initialize failed`);
    }
  };

  init();
}
