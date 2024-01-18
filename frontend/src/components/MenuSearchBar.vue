<template>
  <div>
    <div class="form">
      <i class="fa fa-search"></i>
      <input
        type="text"
        class="form-control form-input"
        placeholder="Search Menu..."
      />
    </div>
  </div>
</template>

<style>
.form {
  position: relative;
}

.form .fa-search {
  position: absolute;
  top: 20px;
  left: 20px;
  color: #9ca3af;
}

.form span {
  position: absolute;
  right: 17px;
  top: 13px;
  padding: 2px;
  border-left: 1px solid #d1d5db;
}

.form-input {
  height: 55px;
  text-indent: 33px;
  border-radius: 0 0px 10px 10px !important;
  border-top: none !important;
}

.form-input:focus {
  box-shadow: none;
  border: none;
}
</style>
