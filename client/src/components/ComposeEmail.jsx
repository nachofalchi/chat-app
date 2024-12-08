// ComposeEmail.jsx
import React, { useState } from 'react';
import './ComposeEmail.css';

export const ComposeEmail = ({ onClose, onSend }) => {
    const [emailData, setEmailData] = useState({
        sender: localStorage.getItem('username'),
        recipient: '',
        subject: '',
        body: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            await onSend(emailData);
            onClose();
        } catch (err) {
            setError('Failed to send email');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="compose-overlay">
            <div className="compose-container">
                <div className="compose-header">
                    <h2>New Message</h2>
                    <button 
                        className="close-button"
                        onClick={onClose}
                    >
                        ×
                    </button>
                </div>

                <form onSubmit={handleSubmit}>
                    <div className="compose-field">
                        <input
                            type="email"
                            placeholder="To"
                            value={emailData.recipient}
                            onChange={(e) => setEmailData({
                                ...emailData,
                                recipient: e.target.value
                            })}
                            required
                        />
                    </div>

                    <div className="compose-field">
                        <input
                            type="text"
                            placeholder="Subject"
                            value={emailData.subject}
                            onChange={(e) => setEmailData({
                                ...emailData,
                                subject: e.target.value
                            })}
                            required
                        />
                    </div>

                    <div className="compose-field">
                        <textarea
                            placeholder="Message"
                            value={emailData.body}
                            onChange={(e) => setEmailData({
                                ...emailData,
                                body: e.target.value
                            })}
                            required
                        />
                    </div>

                    {error && (
                        <div className="error-message">{error}</div>
                    )}

                    <div className="compose-actions">
                        <button 
                            type="submit"
                            disabled={loading}
                        >
                            {loading ? 'Sending...' : 'Send'}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};