import React, { useState, useEffect } from "react";
// Import common API URLs from centralized config (NO hardcoded URLs)
import {
  GET_ALL_STUDENTS_API,
  CREATE_STUDENT_API,
  UPDATE_STUDENT_API,
  DELETE_STUDENT_API,
} from "../config/api";
import "./OverviewPage.css";

// Initial form template
const initialFormState = {
  name: "",
  email: "",
  phonenumber: "",
  department: "",
  address: "",
  python_mark: "",
  java_mark: "",
  database_mark: "",
};

const OverviewPage = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [toast, setToast] = useState(null);

  // Modal State for Create / Edit
  const [modalState, setModalState] = useState({
    isOpen: false,
    mode: "create", // "create" | "edit"
    studentId: null,
  });
  const [formData, setFormData] = useState(initialFormState);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formError, setFormError] = useState(null);

  // Delete Alert / Confirmation Dialog State
  const [deleteDialog, setDeleteDialog] = useState({
    isOpen: false,
    student: null,
    isDeleting: false,
  });

  // Helper to show temporary toast messages
  const showToast = (message, type = "success") => {
    setToast({ message, type });
    setTimeout(() => {
      setToast(null);
    }, 4000);
  };

  // 1. Fetch Students (GET)
  const fetchStudents = async () => {
    setLoading(true);
    try {
      const response = await fetch(GET_ALL_STUDENTS_API);
      if (!response.ok) {
        throw new Error(`Failed to fetch students (HTTP ${response.status})`);
      }
      const result = await response.json();
      const data = Array.isArray(result) ? result : result.data || [];
      setStudents(data);
    } catch (err) {
      console.error("Error fetching students:", err);
      showToast(err.message || "Failed to load student records.", "error");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  // Open Create Modal
  const handleOpenCreate = () => {
    setFormData(initialFormState);
    setFormError(null);
    setModalState({
      isOpen: true,
      mode: "create",
      studentId: null,
    });
  };

  // Open Edit Modal with Pre-filled Student Details
  const handleOpenEdit = (student) => {
    setFormData({
      name: student.name || "",
      email: student.email || "",
      phonenumber: student.phonenumber || "",
      department: student.department || "",
      address: student.address || "",
      python_mark: student.python_mark ?? "",
      java_mark: student.java_mark ?? "",
      database_mark: student.database_mark ?? "",
    });
    setFormError(null);
    setModalState({
      isOpen: true,
      mode: "edit",
      studentId: student.id,
    });
  };

  // Close Create/Edit Modal
  const handleCloseModal = () => {
    if (!isSubmitting) {
      setModalState({ isOpen: false, mode: "create", studentId: null });
      setFormData(initialFormState);
      setFormError(null);
    }
  };

  // Handle Form Input Change
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  // 2 & 3. Submit Form for Create (POST) or Update (PUT)
  const handleSubmitForm = async (e) => {
    e.preventDefault();
    setFormError(null);

    // Basic Validation
    if (
      !formData.name ||
      !formData.email ||
      !formData.phonenumber ||
      !formData.department
    ) {
      setFormError("Please fill in all required fields.");
      return;
    }

    const payload = {
      name: formData.name.trim(),
      email: formData.email.trim(),
      phonenumber: parseInt(formData.phonenumber, 10),
      department: formData.department.trim(),
      address: formData.address.trim(),
      python_mark: parseInt(formData.python_mark, 10) || 0,
      java_mark: parseInt(formData.java_mark, 10) || 0,
      database_mark: parseInt(formData.database_mark, 10) || 0,
    };

    setIsSubmitting(true);
    try {
      let response;
      if (modalState.mode === "create") {
        // CREATE Student API Call
        response = await fetch(CREATE_STUDENT_API, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });
      } else {
        // UPDATE Student API Call
        response = await fetch(UPDATE_STUDENT_API(modalState.studentId), {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });
      }

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(
          errorData.detail ||
            `Failed to ${modalState.mode === "create" ? "create" : "update"} student.`
        );
      }

      const resData = await response.json();
      showToast(
        modalState.mode === "create"
          ? "Student created successfully!"
          : "Student updated successfully!"
      );
      handleCloseModal();
      fetchStudents();
    } catch (err) {
      console.error("Form submit error:", err);
      setFormError(err.message || "An error occurred during submission.");
    } finally {
      setIsSubmitting(false);
    }
  };

  // Open Delete Confirmation Alert Modal
  const handleOpenDelete = (student) => {
    setDeleteDialog({
      isOpen: true,
      student,
      isDeleting: false,
    });
  };

  // Close Delete Confirmation Alert Modal
  const handleCloseDelete = () => {
    if (!deleteDialog.isDeleting) {
      setDeleteDialog({ isOpen: false, student: null, isDeleting: false });
    }
  };

  // 4. Confirm Delete (DELETE)
  const handleConfirmDelete = async () => {
    if (!deleteDialog.student) return;

    setDeleteDialog((prev) => ({ ...prev, isDeleting: true }));
    try {
      const response = await fetch(
        DELETE_STUDENT_API(deleteDialog.student.id),
        {
          method: "DELETE",
        }
      );

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(
          errorData.detail || "Failed to delete student record."
        );
      }

      showToast(`Student #${deleteDialog.student.id} deleted successfully!`);
      handleCloseDelete();
      fetchStudents();
    } catch (err) {
      console.error("Delete error:", err);
      showToast(err.message || "Could not delete student.", "error");
      setDeleteDialog((prev) => ({ ...prev, isDeleting: false }));
    }
  };

  // Filter students based on search term
  const filteredStudents = students.filter((student) => {
    const query = searchTerm.toLowerCase();
    return (
      student.name?.toLowerCase().includes(query) ||
      student.email?.toLowerCase().includes(query) ||
      student.department?.toLowerCase().includes(query) ||
      student.phonenumber?.toString().includes(query)
    );
  });

  // Calculate metrics
  const totalCount = students.length;
  const avgPercentage =
    totalCount > 0
      ? (
          students.reduce((sum, s) => sum + (Number(s.percentage) || 0), 0) /
          totalCount
        ).toFixed(2)
      : "0.00";
  const passCount = students.filter(
    (s) => Number(s.percentage) >= 50
  ).length;

  // Percentage color helper
  const getPercentageClass = (pct) => {
    const val = Number(pct);
    if (val >= 75) return "high";
    if (val >= 60) return "medium";
    if (val >= 40) return "low";
    return "fail";
  };

  return (
    <div className="overview-container">
      {/* Page Header */}
      <div className="overview-header">
        <div className="title-section">
          <h1>Student Academic Overview</h1>
          <p>Batch 4 Full Stack Development • PostgreSQL & FastAPI CRUD Integration</p>
        </div>
        <div className="header-actions">
          <button
            className="btn-refresh"
            onClick={fetchStudents}
            disabled={loading}
          >
            {loading ? "Refreshing..." : "↻ Refresh"}
          </button>
          <button className="btn-create" onClick={handleOpenCreate}>
            + Create Student
          </button>
        </div>
      </div>

      {/* Toast Notification Alert */}
      {toast && (
        <div className={`toast-banner toast-${toast.type}`}>
          <span>
            {toast.type === "success" ? "✓ " : "⚠️ "}
            {toast.message}
          </span>
          <button className="toast-close" onClick={() => setToast(null)}>
            ×
          </button>
        </div>
      )}

      {/* Metric Cards */}
      <div className="stats-grid">
        <div className="stat-card">
          <span className="stat-label">Total Enrolled</span>
          <span className="stat-value">{totalCount}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Class Average</span>
          <span className="stat-value">{avgPercentage}%</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Passing Grade (≥ 50%)</span>
          <span className="stat-value">{passCount} Students</span>
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div className="filter-bar">
        <input
          type="text"
          className="search-input"
          placeholder="🔍 Search by name, email, department, or phone..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <div className="api-badge">
          API: <span>{GET_ALL_STUDENTS_API}</span>
        </div>
      </div>

      {/* Students Table */}
      <div className="table-wrapper">
        {loading ? (
          <div className="state-box">
            <div className="spinner"></div>
            <p>Loading student records...</p>
          </div>
        ) : filteredStudents.length === 0 ? (
          <div className="state-box">
            <p>
              {students.length === 0
                ? "No student records found in the database. Click '+ Create Student' to add one."
                : "No matching student records found for your search filter."}
            </p>
          </div>
        ) : (
          <table className="students-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Student Details</th>
                <th>Department</th>
                <th>Address</th>
                <th>Python</th>
                <th>Java</th>
                <th>Database</th>
                <th>Percentage</th>
                <th style={{ textAlign: "center" }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredStudents.map((student) => {
                const initials = student.name
                  ? student.name
                      .split(" ")
                      .map((n) => n[0])
                      .join("")
                      .substring(0, 2)
                      .toUpperCase()
                  : "ST";

                return (
                  <tr key={student.id}>
                    <td>
                      <strong>#{student.id}</strong>
                    </td>
                    <td>
                      <div className="student-profile">
                        <div className="avatar">{initials}</div>
                        <div className="student-meta">
                          <div className="student-name">{student.name}</div>
                          <div className="student-email">
                            {student.email} • {student.phonenumber}
                          </div>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className="badge badge-dept">
                        {student.department}
                      </span>
                    </td>
                    <td>{student.address || "—"}</td>
                    <td>
                      <span className="mark-pill">{student.python_mark}</span>
                    </td>
                    <td>
                      <span className="mark-pill">{student.java_mark}</span>
                    </td>
                    <td>
                      <span className="mark-pill">{student.database_mark}</span>
                    </td>
                    <td>
                      <span
                        className={`percentage-badge ${getPercentageClass(
                          student.percentage
                        )}`}
                      >
                        {Number(student.percentage).toFixed(2)}%
                      </span>
                    </td>
                    <td>
                      <div className="action-buttons" style={{ justifyContent: "center" }}>
                        <button
                          className="btn-action btn-edit"
                          onClick={() => handleOpenEdit(student)}
                          title="Edit student"
                        >
                          ✎ Edit
                        </button>
                        <button
                          className="btn-action btn-delete"
                          onClick={() => handleOpenDelete(student)}
                          title="Delete student"
                        >
                          🗑 Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
      </div>

      {/* CREATE & EDIT POP-UP MODAL */}
      {modalState.isOpen && (
        <div className="modal-overlay" onClick={handleCloseModal}>
          <div
            className="modal-container"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="modal-header">
              <h2>
                {modalState.mode === "create"
                  ? "Create New Student"
                  : `Edit Student Details (#${modalState.studentId})`}
              </h2>
              <button className="modal-close-btn" onClick={handleCloseModal}>
                ×
              </button>
            </div>

            <form onSubmit={handleSubmitForm}>
              <div className="modal-body">
                {formError && (
                  <div
                    className="toast-banner toast-error"
                    style={{ marginBottom: "16px" }}
                  >
                    <span>⚠️ {formError}</span>
                  </div>
                )}

                <div className="form-grid">
                  <div className="form-group form-group-full">
                    <label>Full Name *</label>
                    <input
                      type="text"
                      name="name"
                      placeholder="e.g. Arun Kumar"
                      value={formData.name}
                      onChange={handleInputChange}
                      required
                    />
                  </div>

                  <div className="form-group">
                    <label>Email Address *</label>
                    <input
                      type="email"
                      name="email"
                      placeholder="e.g. arun@gmail.com"
                      value={formData.email}
                      onChange={handleInputChange}
                      required
                    />
                  </div>

                  <div className="form-group">
                    <label>Phone Number *</label>
                    <input
                      type="number"
                      name="phonenumber"
                      placeholder="e.g. 9876543210"
                      value={formData.phonenumber}
                      onChange={handleInputChange}
                      required
                    />
                  </div>

                  <div className="form-group">
                    <label>Department *</label>
                    <input
                      type="text"
                      name="department"
                      placeholder="e.g. Computer Science"
                      value={formData.department}
                      onChange={handleInputChange}
                      required
                    />
                  </div>

                  <div className="form-group">
                    <label>Address</label>
                    <input
                      type="text"
                      name="address"
                      placeholder="e.g. Chennai"
                      value={formData.address}
                      onChange={handleInputChange}
                    />
                  </div>

                  {/* Marks Block */}
                  <div className="marks-container">
                    <div className="marks-header">Academic Marks (0 - 100)</div>
                    <div className="form-group">
                      <label>Python Mark</label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        name="python_mark"
                        placeholder="0-100"
                        value={formData.python_mark}
                        onChange={handleInputChange}
                      />
                    </div>
                    <div className="form-group">
                      <label>Java Mark</label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        name="java_mark"
                        placeholder="0-100"
                        value={formData.java_mark}
                        onChange={handleInputChange}
                      />
                    </div>
                    <div className="form-group">
                      <label>Database Mark</label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        name="database_mark"
                        placeholder="0-100"
                        value={formData.database_mark}
                        onChange={handleInputChange}
                      />
                    </div>
                  </div>
                </div>
              </div>

              <div className="modal-footer">
                <button
                  type="button"
                  className="btn-secondary"
                  onClick={handleCloseModal}
                  disabled={isSubmitting}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="btn-primary"
                  disabled={isSubmitting}
                >
                  {isSubmitting
                    ? "Submitting..."
                    : modalState.mode === "create"
                    ? "Submit / Create"
                    : "Update Details"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* DELETE CONFIRMATION ALERT POP-UP */}
      {deleteDialog.isOpen && (
        <div className="modal-overlay" onClick={handleCloseDelete}>
          <div
            className="modal-container delete-dialog"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="modal-body">
              <div className="delete-dialog-icon">⚠️</div>
              <h3>Are you sure you want to delete?</h3>
              <p>
                Student record for{" "}
                <span className="delete-student-highlight">
                  "{deleteDialog.student?.name}"
                </span>{" "}
                (ID #{deleteDialog.student?.id}) will be permanently removed.
              </p>
            </div>
            <div
              className="modal-footer"
              style={{ justifyContent: "center", background: "transparent" }}
            >
              <button
                type="button"
                className="btn-secondary"
                onClick={handleCloseDelete}
                disabled={deleteDialog.isDeleting}
              >
                Cancel
              </button>
              <button
                type="button"
                className="btn-danger"
                onClick={handleConfirmDelete}
                disabled={deleteDialog.isDeleting}
              >
                {deleteDialog.isDeleting ? "Deleting..." : "Submit & Delete"}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default OverviewPage;
