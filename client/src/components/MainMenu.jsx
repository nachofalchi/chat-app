import React, { useState } from 'react';
import './MainMenu.css';
import SearchIcon from '@mui/icons-material/Search';

export const MainMenu = () => {
    const [selectedEmail, setSelectedEmail] = useState(null);

    // Mock data
    const emails = [
        { id: 1, from: 'john@example.com', subject: 'Meeting Tomorrow', content: 'Hi, just confirming...', date: '10:30 AM' },
        { id: 2, from: 'alice@example.com', subject: 'Project Update', content: 'The latest changes...', date: '9:15 AM' },
    ];
    const handleEmailClick = (email) => {
        setSelectedEmail(email);
    };

    return (
        <div className="mail-container">
            {/* Sidebar */}
            <div className="sidebar">
                <button className="compose-btn">Compose</button>
                <ul className="folder-list">
                    <li className="active">Inbox</li>
                    <li>Sent</li>
                    <li>Drafts</li>
                    <li>Trash</li>
                </ul>
            </div>

            {/* Email List */}
            <div className="email-list">
            <div className="search-bar">
                <input type="text" placeholder="Search mail..." />
                <button className="search-button">
                    <SearchIcon className="search-icon" />
                </button>
            </div>
                {emails.map(email => (
                    <div key={email.id} className="email-item" onClick={() => handleEmailClick(email)}>
                        <div className="email-sender">{email.from}</div>
                        <div className="email-subject">{email.subject}</div>
                        <div className="email-date">{email.date}</div>
                    </div>
                ))}
            </div>

            {/* Email View */}
            <div className="email-view">
                {selectedEmail ? (
                    <div className="email-detail">
                        <h3>{selectedEmail.subject}</h3>
                        <div className="email-header">
                            <span>From: {selectedEmail.from}</span>
                            <span>{selectedEmail.date}</span>
                        </div>
                        <div className="email-body">
                            {selectedEmail.content}
                        </div>
                    </div>
                ) : (
                    <div className="no-email-selected">
                        Select an email to read
                    </div>
                )}
            </div>
        </div>
    );
}