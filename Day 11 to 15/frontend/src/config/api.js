// Common API Configuration for Backend Integration
// Modify API_BASE_URL if your backend runs on a different port or host.
export const API_BASE_URL = "http://localhost:8000";

// Student CRUD Endpoints
export const GET_ALL_STUDENTS_API = `${API_BASE_URL}/get-all-students`;
export const CREATE_STUDENT_API = `${API_BASE_URL}/create-student`;
export const GET_STUDENT_BY_ID_API = (id) => `${API_BASE_URL}/get-student/${id}`;
export const UPDATE_STUDENT_API = (id) => `${API_BASE_URL}/update-student/${id}`;
export const DELETE_STUDENT_API = (id) => `${API_BASE_URL}/delete-student/${id}`;

// User Registration & Authentication Endpoints
export const REGISTER_USER_API = `${API_BASE_URL}/register`;
export const LOGIN_USER_API = `${API_BASE_URL}/login`;
export const GET_USER_BY_ID_API = (id) => `${API_BASE_URL}/user/${id}`;

