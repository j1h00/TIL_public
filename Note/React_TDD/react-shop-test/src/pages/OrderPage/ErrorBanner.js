import React from "react";

export default function ErrorBanner({ message }) {
  let errorMessage = message || "에러입니다.";

  return (
    <div
      data-testid="error-banner"
      style={{ backgroundColor: "red", color: "white" }}
    >
      {errorMessage}
    </div>
  );
}
