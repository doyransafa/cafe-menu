import axiosInstance from "../http-common";

class ProductDataService {
  getAll() {
    return axiosInstance.get("/products");
  }

  get(id: number) {
    return axiosInstance.get(`/products/${id}`);
  }

  getSubCategory(id: number) {
    return axiosInstance.get(`/products/?sub_category=${id}`);
  }

  create(data: any) {
    return axiosInstance.post("/products/", data);
  }

  update(id: number, data: any) {
    return axiosInstance.put(`/products/${id}/`, data);
  }

  delete(id: number) {
    return axiosInstance.delete(`/products/${id}`);
  }

  deleteAll() {
    return axiosInstance.delete(`/products`);
  }
}

export default new ProductDataService();
