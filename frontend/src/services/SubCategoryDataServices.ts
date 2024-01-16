import axiosInstance from "../http-common";

class SubCategoryDataService {
  getAll() {
    return axiosInstance.get("/subcategories");
  }

  get(id: number) {
    return axiosInstance.get(`/subcategories/${id}`);
  }

  create(data: any) {
    return axiosInstance.post("/subcategories/", data);
  }

  update(id: number, data: any) {
    return axiosInstance.put(`/subcategories/${id}/`, data);
  }

  delete(id: number) {
    return axiosInstance.delete(`/subcategories/${id}`);
  }

  deleteAll() {
    return axiosInstance.delete(`/subcategories`);
  }
}

export default new SubCategoryDataService();
