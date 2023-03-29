<template>
  <main class="container-full">
    <div id="x-main" class="container-fluid mt-5 p-3" style="min-height: 550px">
      <div class="row">
        <div class="col-8">
          <h3 class="card-title">Beneficiaries</h3>
          <img style="width: 200px" src="/static/img/spirulina-fnd.png" />
        </div>
        <div class="col-4">
          <div class="card login-card m-4 bg-secondary text-light">
            <div class="card-body">
              <h5 class="card-title">Login</h5>
              <form1>
                <div class="form-group">
                  <label for="usernameInput">Username</label>
                  <input
                    type="text"
                    class="form-control"
                    id="usernameInput"
                    placeholder="Enter username"
                  />
                </div>
                <div class="form-group mt-2">
                  <label for="passwordInput">Password</label>
                  <input
                    type="password"
                    class="form-control"
                    id="passwordInput"
                    placeholder="Enter password"
                  />
                </div>
                <button
                  type="submit"
                  class="mt-4 btn btn-primary"
                  data-nav="admin.dashboard"
                >
                  Login
                </button>
                <!-- <button type="submit" class="mt-4 btn btn-primary" data-nav="ngo.dashboard">NGO</button> -->
              </form1>
            </div>
          </div>

          <div class="card login-card m-4 bg-secondary text-light">
            <div class="card-body">
              <h5 class="card-title">Supported by</h5>
              <a href="https://www.emids.com/" target="_blank"
                ><img style="width: 160px" src="/static/img/emids-logo.png" class="me-3"
              /></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
