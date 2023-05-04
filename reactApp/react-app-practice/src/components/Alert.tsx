import React from "react";

interface Props {
  children: React.ReactNode;
}
export default function Alert({ children }: Props) {
  const [alert, setAlert] = React.useState(false);

  function alertData() {
    console.log("coming");
    return (
      <div className="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Holy guacamole!</strong> You should check in on some of those
        fields below.
        <button
          type="button"
          className="btn-close"
          data-bs-dismiss="alert"
          aria-label="Close"
          onClick={() => setAlert(false)}
        ></button>
      </div>
    );
  }

  function alertShow() {
    return alert ? alertData() : null;
  }

  return (
    <div>
      {alertShow()}
      <button
        type="button"
        className="btn btn-primary"
        onClick={() => setAlert(true)}
      >
        My Button
      </button>
    </div>
  );
}
