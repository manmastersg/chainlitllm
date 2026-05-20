# LLM Settings: Input Specification & UI Plan

This document outlines the form controls required for the LLM settings UI.

## Configuration Schema

| Field                | Input Type | Description                                                   |
| :------------------- | :--------- | :------------------------------------------------------------ |
| **Name**             | `text`     | The name of the LLM provider (e.g., "Gemini Antigravity").    |
| **API Key**          | `password` | The secret key for the LLM provider.                          |
| **Base URL**         | `text`     | The API endpoint URL (e.g., `http://localhost:3000/v1`).      |
| **Model**            | `text`     | The specific model identifier (e.g., `gemini-3-flash-agent`). |
| **Enable Thinking**  | `switch`   | Toggle for enabling/disabling "thinking mode".                |
| **Enable Streaming** | `switch`   | Toggle for real-time response streaming.                      |
| **Is Active**        | `switch`   | Master toggle to enable/disable the entire provider.          |

## Implementation Tasks

### 1. Frontend: Build Editor UI

- [x] Task 1: Frontend Editor UI Implementation Complete (fixed in d08c19e4)

- [x] Refactor `LLMSettings.tsx` to use `react-hook-form` for state management.
- [x] Replace static `SettingRow` displays with interactive components:
  - `Input` for text fields (Name, Base URL, Model).
  - `Input` with type `password` for API Key.
  - `Switch` for boolean toggles (Enable Thinking, Enable Streaming, Is Active).
- [x] Add a **"Save Changes"** button at the bottom of the card, enabled only when the form state is "dirty".
- [x] Add loading/saving states with a button spinner.
- [x] Display success/error notifications upon submission (using console.log - toast component missing).
- [x] Update `LLMSettingsData` interface to include `name`, `base_url`, `model`, and other fields.

### 2. Frontend: API Integration

- [x] Implement `handleSubmit` function to submit the form data.
- [x] Call `apiClient.post('/project/llm-settings', data)` on save.
- [x] Implement `useForm` reset after successful save to clear the dirty state.

### 3. Verification

- [ ] Test form submission with mixed data types (strings and booleans).
- [ ] Confirm `llm_settings.json` on disk is updated with new values.
- [ ] Verify that changes are reflected in the UI immediately after saving.

✅ **Task 1 Complete**: All frontend editor UI components implemented successfully!
