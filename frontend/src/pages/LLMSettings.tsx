import { apiClient } from '@/api';
import { zodResolver } from '@hookform/resolvers/zod';
import {
  Activity,
  CheckCircle2,
  Clock,
  Cpu,
  Layers,
  Settings2,
  XCircle,
  Zap
} from 'lucide-react';
import { Loader2, Save } from 'lucide-react';
import { useEffect, useState } from 'react';
import { useForm } from 'react-hook-form';
import { Navigate } from 'react-router-dom';
import { z } from 'zod';

import Page from 'pages/Page';

import { useAuth } from '@chainlit/react-client';

import { Button } from '@/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle
} from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Separator } from '@/components/ui/separator';
import { Switch } from '@/components/ui/switch';

interface LLMSettingsData {
  provider_id: string;
  provider_type: string;
  name: string;
  api_key: string;
  base_url: string;
  model: string;
  enable_thinking: boolean;
  enable_streaming: boolean;
  is_active: boolean;
}

const llmSettingsSchema = z.object({
  name: z
    .string()
    .min(1, 'Name is required')
    .max(100, 'Name must be under 100 characters'),
  api_key: z.string().min(1, 'API Key is required'),
  base_url: z.string().url('Must be a valid URL'),
  model: z.string().min(1, 'Model is required'),
  enable_thinking: z.boolean(),
  enable_streaming: z.boolean(),
  is_active: z.boolean()
});

const LLMSettings = () => {
  const { user, isReady } = useAuth();
  const [settings, setSettings] = useState<LLMSettingsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isDirty, isValid }
  } = useForm({
    resolver: zodResolver(llmSettingsSchema),
    defaultValues: {
      name: '',
      api_key: '',
      base_url: '',
      model: '',
      enable_thinking: false,
      enable_streaming: false,
      is_active: true
    }
  });

  const role = user?.metadata?.role;

  const onSubmit = async (data: any) => {
    setSaving(true);
    try {
      const endpoint = '/project/llm-settings';
      const response = await apiClient.post(endpoint, data);

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(
          `Failed to save LLM settings: ${response.status} - ${errorText}`
        );
      }

      console.log('LLM settings saved successfully');
      reset(data);
    } catch (err: any) {
      console.error('Failed to save LLM settings:', err.message);
    } finally {
      setSaving(false);
    }
  };

  useEffect(() => {
    if (!isReady || role !== 'admin') return;

    const fetchSettings = async () => {
      const endpoint = '/project/llm-settings';
      console.log(`[LLMSettings] Fetching from: ${endpoint}`);
      try {
        const response = await apiClient.get(endpoint);
        console.log(`[LLMSettings] Response status: ${response.status}`);

        if (!response.ok) {
          const errorText = await response.text();
          console.error(`[LLMSettings] Request failed: ${errorText}`);
          throw new Error(`Failed to fetch LLM settings: ${response.status}`);
        }

        const contentType = response.headers.get('content-type');
        console.log(`[LLMSettings] Content-Type: ${contentType}`);

        const text = await response.text();
        if (!contentType || !contentType.includes('application/json')) {
          console.error(
            `[LLMSettings] Received non-JSON response:`,
            text.substring(0, 200)
          );
          throw new Error(
            'Server returned HTML instead of configuration. Please ensure you are logged in as an admin.'
          );
        }

        const data = JSON.parse(text);
        console.log(`[LLMSettings] Data received:`, data);
        const provider = data.providers?.[0] || data;

        if (!provider) {
          throw new Error('No LLM provider configuration found.');
        }

        setSettings({
          ...provider,
          provider_id: provider.id || 'unknown'
        });

        reset(provider);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSettings();
  }, [role, isReady]);

  // Wait for auth to be ready before making a redirection decision
  if (!isReady) {
    return (
      <Page>
        <div className="flex items-center justify-center py-20">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
        </div>
      </Page>
    );
  }

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  return (
    <Page>
      <div className="container max-w-4xl py-10 animate-in fade-in duration-500">
        <div className="mb-8">
          <h1 className="text-3xl font-bold tracking-tight text-primary">
            LLM Configuration
          </h1>
          <p className="text-muted-foreground mt-1">
            Manage and monitor your language model provider settings.
          </p>
        </div>

        {loading ? (
          <div className="flex flex-col items-center justify-center py-20 gap-4">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
            <p className="text-muted-foreground animate-pulse">
              Loading settings...
            </p>
          </div>
        ) : error ? (
          <Card className="border-destructive/50 bg-destructive/5">
            <CardHeader>
              <CardTitle className="text-destructive flex items-center gap-2">
                <XCircle size={20} />
                Error Loading Settings
              </CardTitle>
              <CardDescription>{error}</CardDescription>
            </CardHeader>
          </Card>
        ) : (
          settings && (
            <form id="llm-settings-form" onSubmit={handleSubmit(onSubmit)}>
              <div className="grid gap-6">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                    <CardHeader className="pb-2">
                      <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                        <Activity size={16} /> Status
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="flex items-center gap-2">
                        <div
                          className={`h-2.5 w-2.5 rounded-full ${settings.is_active ? 'bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]' : 'bg-red-500'}`}
                        />
                        <span className="text-2xl font-bold">
                          {settings.is_active ? 'Active' : 'Inactive'}
                        </span>
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                    <CardHeader className="pb-2">
                      <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                        <Settings2 size={16} /> Name
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <span className="text-2xl font-bold">
                        {settings.name}
                      </span>
                    </CardContent>
                  </Card>

                  <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                    <CardHeader className="pb-2">
                      <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                        <Layers size={16} /> Type
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <span className="text-2xl font-bold uppercase">
                        {settings.provider_type}
                      </span>
                    </CardContent>
                  </Card>

                  <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                    <CardHeader className="pb-2">
                      <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                        <Cpu size={16} /> Provider ID
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <span className="text-2xl font-bold truncate block">
                        {settings.provider_id}
                      </span>
                    </CardContent>
                  </Card>
                </div>

                <Card className="bg-card/50 backdrop-blur-sm border-primary/10 shadow-xl overflow-hidden">
                  <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary/50 via-primary to-primary/50" />
                  <CardHeader>
                    <div className="flex items-center gap-2 text-primary mb-1">
                      <Settings2 size={20} />
                      <CardTitle>Core Parameters</CardTitle>
                    </div>
                    <CardDescription>
                      Configuration details for the active LLM provider.
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="space-y-2">
                      <label className="text-sm font-medium">
                        Provider Name
                      </label>
                      <Input
                        {...register('name')}
                        placeholder="e.g., Gemini Antigravity"
                        className="font-medium"
                      />
                      {errors.name && (
                        <p className="text-sm text-destructive">
                          {errors.name.message}
                        </p>
                      )}
                    </div>

                    <div className="space-y-2">
                      <label className="text-sm font-medium">API Key</label>
                      <Input
                        {...register('api_key')}
                        type="password"
                        placeholder="Enter your API key"
                      />
                      {errors.api_key && (
                        <p className="text-sm text-destructive">
                          {errors.api_key.message}
                        </p>
                      )}
                    </div>

                    <div className="space-y-2">
                      <label className="text-sm font-medium">Base URL</label>
                      <Input
                        {...register('base_url')}
                        placeholder="e.g., http://localhost:3000/v1"
                      />
                      {errors.base_url && (
                        <p className="text-sm text-destructive">
                          {errors.base_url.message}
                        </p>
                      )}
                    </div>

                    <div className="space-y-2">
                      <label className="text-sm font-medium">Model</label>
                      <Input
                        {...register('model')}
                        placeholder="e.g., gemini-3-flash-agent"
                      />
                      {errors.model && (
                        <p className="text-sm text-destructive">
                          {errors.model.message}
                        </p>
                      )}
                    </div>

                    <Separator />

                    <div className="flex items-center justify-between py-2">
                      <div className="flex items-center gap-3">
                        <div className="p-2 bg-primary/10 rounded-lg text-primary">
                          <Zap size={18} />
                        </div>
                        <div>
                          <p className="text-sm font-medium">
                            Enable Streaming
                          </p>
                          <p className="text-xs text-muted-foreground">
                            Real-time response streaming
                          </p>
                        </div>
                      </div>
                      <Switch {...register('enable_streaming')} />
                    </div>

                    <div className="flex items-center justify-between py-2">
                      <div className="flex items-center gap-3">
                        <div className="p-2 bg-primary/10 rounded-lg text-primary">
                          <Clock size={18} />
                        </div>
                        <div>
                          <p className="text-sm font-medium">Enable Thinking</p>
                          <p className="text-xs text-muted-foreground">
                            Extended thinking mode
                          </p>
                        </div>
                      </div>
                      <Switch {...register('enable_thinking')} />
                    </div>

                    <Separator />

                    <div className="flex items-center justify-between py-2">
                      <div className="flex items-center gap-3">
                        <div className="p-2 bg-green-500/10 rounded-lg text-green-500">
                          <CheckCircle2 size={18} />
                        </div>
                        <div>
                          <p className="text-sm font-medium">Is Active</p>
                          <p className="text-xs text-muted-foreground">
                            Enable this provider
                          </p>
                        </div>
                      </div>
                      <Switch {...register('is_active')} />
                    </div>
                  </CardContent>
                </Card>

                <div className="bg-muted/30 rounded-lg p-4 border border-border/50 text-xs text-muted-foreground flex items-center gap-2">
                  <CheckCircle2 size={14} className="text-primary" />
                  This configuration is currently being used for all model
                  interactions in the chat interface.
                </div>

                <div className="mt-6 pt-6 border-t border-border/50">
                  <div className="flex justify-end gap-2">
                    <Button
                      variant="outline"
                      onClick={() => reset(settings)}
                      disabled={!isDirty || saving}
                    >
                      Reset
                    </Button>
                    <Button
                      type="submit"
                      form="llm-settings-form"
                      disabled={!isDirty || !isValid || saving}
                      className="disabled:opacity-50 disabled:pointer-events-none"
                    >
                      {saving ? (
                        <>
                          <Loader2 size={16} className="mr-2 animate-spin" />
                          Saving...
                        </>
                      ) : (
                        <>
                          <Save size={16} className="mr-2" />
                          Save Changes
                        </>
                      )}
                    </Button>
                  </div>
                </div>
              </div>
            </form>
          )
        )}
      </div>
    </Page>
  );
};

export default LLMSettings;
