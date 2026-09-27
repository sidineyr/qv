// Recover from malformed or outdated browser data without blocking the survey.
function loadStoredValue(key, fallback, isValid) {
  try {
    const raw = localStorage.getItem(key);
    if (raw === null) return fallback;
    const value = JSON.parse(raw);
    if (isValid(value)) return value;
  } catch (_) {
    // A malformed value should not prevent the page from loading.
  }
  try { localStorage.removeItem(key); } catch (_) {}
  return fallback;
}
