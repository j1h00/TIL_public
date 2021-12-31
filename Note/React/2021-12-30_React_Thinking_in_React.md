# TIL : Thinking in React

React 로 상품들을 검색할 수 있는 데이터 테이블을 만드는 과정을 함께 보자!

### 목업으로 시작하기 

JSON API 와 목업을 받았다고 가정해보자!

![목업](https://ko.reactjs.org/static/1071fbcc9eed01fddc115b41e193ec11/d4770/thinking-in-react-mock.png)

```json
[
  {category: "Sporting Goods", price: "$49.99", stocked: true, name: "Football"},
  {category: "Sporting Goods", price: "$9.99", stocked: true, name: "Baseball"},
  {category: "Sporting Goods", price: "$29.99", stocked: false, name: "Basketball"},
  {category: "Electronics", price: "$99.99", stocked: true, name: "iPod Touch"},
  {category: "Electronics", price: "$399.99", stocked: false, name: "iPhone 5"},
  {category: "Electronics", price: "$199.99", stocked: true, name: "Nexus 7"}
];
```

### 1단계 : UI 를 컴포넌트 계층으로 나누기 

모든 컴포넌트의 주변에 박스를 그리고, 각각에 이름을 붙이자!

디자이너의 Photoshop 레이어 이름이 React 컴포넌트 이름이 될 수 있다. 

어떤 것이 컴포넌트가 되어야할 지 어떻게 아는가? 새로운 함수나 객체를 만들 때 처럼, 단일 책임 원칙을 둔다. 하나의 컴포넌트는 한 가지의 일을 하는게 이상적이다. 

주로 JSON 데이터를 유저에게 보여주기 때문에, 데이터 모델이 적절하다면, 각 컴포넌트가 데이터 모델의 한 조각을 나타내도록 분리하는 것도 방법이다. 

![Diagram showing nesting of components](https://ko.reactjs.org/static/9381f09e609723a8bb6e4ba1a7713b46/90cbd/thinking-in-react-components.png)

1. `FilterableProductTable` : 예시 전체 
2. `SearchBar` : 모든 유저의 입력을 받음
3. `ProductTable` : 유저의 입력을 기반으로 데이터 콜렉션을 필터링해서 보여줌
4. `ProductCategoryRow` : 각 카테고리의 헤더를
5. `ProductRow` : 각각의 제품에 해당하는 행

이를 계층 구조로 나열하면

- `FilterableProductTable`
  - `SearchBar`
  - `ProductTable`
    - `ProductCategoryRow`
    - `ProductRow`

### 2단계 : React 로 정적인 버전 만들기

실제 구현! 가장 쉬운 방법은 데이터 모델로 렌더링은 되지만 아무 동작 없는 버전을 먼저 만드는 것이다. 

정적 버전을 만들 때엔, state 를 사용하지 않는다. state 는 상호작용, 즉 시간이 지남에 따라 데이터가 바뀌는 때에 사용하므로 필요하지 않다. 

```react
class ProductCategoryRow extends React.Component {
  render() {
    const category = this.props.category;
    return (
      <tr>
        <th colSpan="2">
          {category}
        </th>
      </tr>
    );
  }
}

class ProductRow extends React.Component {
  render() {
    const product = this.props.product;
    const name = product.stocked ?
      product.name :
      <span style={{color: 'red'}}>
        {product.name}
      </span>;

    return (
      <tr>
        <td>{name}</td>
        <td>{product.price}</td>
      </tr>
    );
  }
}

class ProductTable extends React.Component {
  render() {
    const rows = [];
    let lastCategory = null;
    
    this.props.products.forEach((product) => {
      if (product.category !== lastCategory) {
        rows.push(
          <ProductCategoryRow
            category={product.category}
            key={product.category} />
        );
      }
      rows.push(
        <ProductRow
          product={product}
          key={product.name} />
      );
      lastCategory = product.category;
    });

    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    );
  }
}

class SearchBar extends React.Component {
  render() {
    return (
      <form>
        <input type="text" placeholder="Search..." />
        <p>
          <input type="checkbox" />
          {' '}
          Only show products in stock
        </p>
      </form>
    );
  }
}

class FilterableProductTable extends React.Component {
  render() {
    return (
      <div>
        <SearchBar />
        <ProductTable products={this.props.products} />
      </div>
    );
  }
}


const PRODUCTS = [
  {category: 'Sporting Goods', price: '$49.99', stocked: true, name: 'Football'},
  {category: 'Sporting Goods', price: '$9.99', stocked: true, name: 'Baseball'},
  {category: 'Sporting Goods', price: '$29.99', stocked: false, name: 'Basketball'},
  {category: 'Electronics', price: '$99.99', stocked: true, name: 'iPod Touch'},
  {category: 'Electronics', price: '$399.99', stocked: false, name: 'iPhone 5'},
  {category: 'Electronics', price: '$199.99', stocked: true, name: 'Nexus 7'}
];
 
ReactDOM.render(
  <FilterableProductTable products={PRODUCTS} />,
  document.getElementById('container')
);

```

- 위와 같이, 정적인 버전은 오직 데이터 렌더링을 위해 만들어지기 때문에 `render()` 메서드만 가지고 있다. 
- 계층 구조의 최상단 컴포넌트는 prop 으로 데이터 모델을 받고, 오직 이 데이터 모델의 변경에 의해서만 `ReactDOM.render()` 가 다시 호출되어 UI 가 업데이트 된다. 

### 3단계 : Identify The Minimal (but complete) Representation Of UI State

애플리케이션에서 필요로 하는 변경 가능한 state 의 최소 집합을 생각해보아야 한다. 

이 때 핵심은 ***중복 배제 원칙 !!!*** 

필요로 하는 가장 최소한의 state 를 찾고, 나머지는 필요에 따라 그때 그때 계산되도록 한다. 예를 들어 TODO 리스트에서 TODO 아이템의 개수를 표현하는 state 는 별도로 만들지 말고, TODO 아이템을 저장하는 배열만 만들어 그때 그때 길이를 가져오면 된다. 

 



