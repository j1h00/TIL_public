import Type from "../Type";
import { render, screen } from "@testing-library/react";

test("displays products images from server", async () => {
  render(<Type orderType="products" />);

  // 이미지 찾기
  const productImages = await screen.findAllByRole("img", {
    name: /product$/i,
  });
  expect(productImages).toHaveLength(2);

  const altText = productImages.map((element) => element.alt);
  expect(altText).toEqual(["America product", "England product"]);
});
