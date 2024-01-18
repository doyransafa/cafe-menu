import axiosInstance from "../http-common";

class CategoryDataService {
  getAll() {
    return axiosInstance.get("/categories");
  }

  get(id: number) {
    return axiosInstance.get(`/categories/${id}`);
  }

  create(data: any) {
    return axiosInstance.post("/categories/", data);
  }

  update(id: number, data: any) {
    return axiosInstance.put(`/categories/${id}/`, data);
  }

  delete(id: number) {
    return axiosInstance.delete(`/categories/${id}`);
  }

  deleteAll() {
    return axiosInstance.delete(`/categories`);
  }
}

export default new CategoryDataService();
