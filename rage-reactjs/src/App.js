import React from "react";

function App() {
  return (
    <div className="container-fluid" style={{ marginTop: "20%" }}>
      <div className="row">
        <div className="col-12 d-flex justify-content-end">
          <div className="p-5">
            <div className="p-3" style={{ width: "100%" }}> {/* backgroundColor: '#1e1e1edb'*/}

              <ul class="list-group">
                <li id="kill" class="list-group-item d-flex justify-content-between align-items-center bg-transparent text-light border-warning mb-3">
                  Kill me
                  <span class="badge bg-warning text-dark fs-5 rounded-pill">F4</span>
                </li>

                <li id="carspawn" class="list-group-item d-flex justify-content-between align-items-center bg-transparent text-light border-warning mb-3">
                  Spawn car
                  <span class="badge bg-warning text-dark fs-5 rounded-pill">F2</span>
                </li>
              </ul>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
