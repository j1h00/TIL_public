"use strict";

/* global CustomError, getLikedBrands, getTopBrandsForGender */

function solution(U, N) {
  return new Promise((resolve, reject) => {
    // Resolve the promise with the result
    Promise.all([getLikedBrands(U.id), getTopBrandsForGender(U.gender)])
      .then(([likedBrands, topBrandsForGender]) => {
        const uniqueBrands = likedBrands.map((brand) => brand.name);
        // push only if unique
        topBrandsForGender.forEach((brand) => {
          if (!uniqueBrands.includes(brand.name)) {
            uniqueBrands.push(brand.name);
          }
        });
        return uniqueBrands;
      })
      .then((topBrands) => {
        if (topBrands) {
          if (topBrands.length < N) reject(new CustomError("Not enough data"));

          resolve(topBrands.slice(0, N).map((brandName) => brandName));
        }
      });
  });
}
