import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './MainMenu.css';
import SearchIcon from '@mui/icons-material/Search';

export const MainMenu = () => {
    const [selectedEmail, setSelectedEmail] = useState(null);
    const [emails, setEmails] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [username] = useState(localStorage.getItem('username'));
    const navigate = useNavigate();

    // Logout
    const handleLogout = () => {
        localStorage.removeItem('token'); 
        navigate('/');                     
    };

    // Fetch emails
    useEffect(() => {
        const fetchEmails = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await axios.get('http://localhost:8000/email/inbox', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                setEmails(response.data.emails);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching emails:', error);
                setError('Could not load emails');
                setLoading(false);
            }
        };
        
        fetchEmails();
    }, []);

    // Handle email click
    const handleEmailClick = (email) => {
        setSelectedEmail(email);
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    return (
        <div className="mail-container">
            {/* Top Bar */}
            <div className="top-bar">
                <div className='app-name'>Mail App</div>
                <div className="search-bar">
                    <input type="text" placeholder="Search mail..." />
                    <button className="search-button">
                        <SearchIcon className="search-icon" />
                    </button>
                </div>
                <div className="user-info">{username}</div>
            </div>
            {/* Sidebar */}
            <div className="sidebar">
                <button className="compose-btn">Compose</button>
                <ul className="folder-list">
                    <li className="active">Inbox</li>
                    <li>Sent</li>
                    <li>Drafts</li>
                    <li>Trash</li>
                </ul>
                <button 
                    className="logout-btn"
                    onClick={handleLogout}
                >
                Logout</button>
            </div>

            {/* Email List */}
            <div className="email-list">
                <div className='email-control-buttons'>
                    <button className="control-button">
                        <span className="control-icon">🗑️</span>
                        Delete
                    </button>
                    <button className="control-button">
                        <span className="control-icon">📨</span>
                        Mark as Read
                    </button>
                    <button className="control-button">
                        <span className="control-icon">📁</span>
                        Move to
                    </button>
                </div>
                <div className="email-list-container">
                    {emails.map(email => (
                        <div key={email.id} className="email-item" onClick={() => handleEmailClick(email)}>
                            <div className="email-sender">{email.sender}</div>
                            <div className="email-subject">{email.subject}</div>
                            <div className="email-date">{email.timestamp}</div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Email View */}
            <div className="email-view">
                {selectedEmail ? (
                    <div className="email-detail">
                        <h3>{selectedEmail.subject}</h3>
                        <div className="email-header">
                            <span>From: {selectedEmail.sender}</span>
                            <span>{selectedEmail.timestamp}</span>
                        </div>
                        <div className="email-body">
                            {selectedEmail.body}
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