# LLM Settings: Input Specification & UI Plan

This document outlines the form controls required for the LLM settings UI.

## Configuration Schema

| Field                | Input Type | Description                                                   |
| :------------------- | :--------- | :------------------------------------------------------------ |
| **API Key**          | `password` | The secret key for the LLM provider.                          |
| **Base URL**         | `text`     | The API endpoint URL (e.g., `http://localhost:3000/v1`).      |
| **Model**            | `text`     | The specific model identifier (e.g., `gemini-3-flash-agent`). |
| **Enable Thinking**  | `switch`   | Toggle for enabling/disabling "thinking mode".                |
| **Enable Streaming** | `switch`   | Toggle for real-time response streaming.                      |
| **Is Active**        | `switch`   | Master toggle to enable/disable the entire provider.          |

## Implementation Tasks

### 1. Frontend: Build Editor UI

- [ ] Refactor `LLMSettings.tsx` to use `react-hook-form` for state management.
- [ ] Replace static `SettingRow` displays with interactive components:
  - `Input` for text fields (Base URL, Model).
  - `Input` with type `password` for API Key.
  - `Switch` for boolean toggles (Enable Thinking, Enable Streaming, Is Active).
- [ ] Add a **"Save Changes"** button at the bottom of the card, enabled only when the form state is "dirty".
- [ ] Add loading/saving states with a button spinner.
- [ ] Display toast success/error notifications upon submission.

### 2. Frontend: API Integration

- [ ] Implement `handleSubmit` function to submit the form data.
- [ ] Call `apiClient.post('/project/llm-settings', data)` on save.
- [ ] Implement `useForm` reset after successful save to clear the dirty state.

### 3. Verification

- [ ] Test form submission with mixed data types (strings and booleans).
- [ ] Confirm `llm_settings.json` on disk is updated with new values.
- [ ] Verify that changes are reflected in the UI immediately after saving.
